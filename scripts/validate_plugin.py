#!/usr/bin/env python3
"""Validate every plugin in the plugin-tools-for-ai marketplace.

Reads .claude-plugin/marketplace.json, then for each listed plugin checks that:
  - its plugin.json manifest is valid JSON,
  - every agent (agents/*.md) has frontmatter with name + description, and the
    name matches the filename,
  - every skill (skills/*/SKILL.md) has frontmatter with name + description, and
    the name matches the directory.

Run from the repo root:  python3 scripts/validate_plugin.py
Exit code 0 = all good, 1 = problems found (used by CI).
"""
from __future__ import annotations

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def parse_frontmatter(path: str):
    """Return (frontmatter_dict, body) or (None, text) if no frontmatter."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if not m:
        return None, text
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            key, val = line.split(":", 1)
            fm[key.strip()] = val.strip()
    return fm, m.group(2)


def validate_plugin(source: str, problems: list[str]) -> tuple[int, int]:
    """Validate one plugin rooted at `source` (relative to repo root)."""
    base = os.path.normpath(os.path.join(ROOT, source))
    label = source

    # Manifest
    manifest = os.path.join(base, ".claude-plugin", "plugin.json")
    if not os.path.exists(manifest):
        problems.append(f"[{label}] missing .claude-plugin/plugin.json")
    else:
        try:
            json.load(open(manifest, encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            problems.append(f"[{label}] plugin.json: {exc}")

    # Agents
    n_agents = 0
    agents_dir = os.path.join(base, "agents")
    if os.path.isdir(agents_dir):
        for a in sorted(f for f in os.listdir(agents_dir) if f.endswith(".md")):
            n_agents += 1
            fm, body = parse_frontmatter(os.path.join(agents_dir, a))
            if fm is None:
                problems.append(f"[{label}] agent {a}: no frontmatter")
                continue
            if not fm.get("name"):
                problems.append(f"[{label}] agent {a}: missing 'name'")
            if not fm.get("description"):
                problems.append(f"[{label}] agent {a}: missing 'description'")
            if fm.get("name") and fm["name"] != a[:-3]:
                problems.append(f"[{label}] agent {a}: name != filename")
            if len(body.strip()) < 50:
                problems.append(f"[{label}] agent {a}: body too short")

    # Skills
    n_skills = 0
    skills_dir = os.path.join(base, "skills")
    if os.path.isdir(skills_dir):
        for s in sorted(
            d for d in os.listdir(skills_dir)
            if os.path.isdir(os.path.join(skills_dir, d))
        ):
            n_skills += 1
            path = os.path.join(skills_dir, s, "SKILL.md")
            if not os.path.exists(path):
                problems.append(f"[{label}] skill {s}: missing SKILL.md")
                continue
            fm, body = parse_frontmatter(path)
            if fm is None:
                problems.append(f"[{label}] skill {s}: no frontmatter")
                continue
            if not fm.get("name"):
                problems.append(f"[{label}] skill {s}: missing 'name'")
            if not fm.get("description"):
                problems.append(f"[{label}] skill {s}: missing 'description'")
            if fm.get("name") and fm["name"] != s:
                problems.append(f"[{label}] skill {s}: name != directory")
            if len(body.strip()) < 50:
                problems.append(f"[{label}] skill {s}: body too short")

    return n_agents, n_skills


def main() -> int:
    problems: list[str] = []

    market_path = os.path.join(ROOT, ".claude-plugin", "marketplace.json")
    try:
        market = json.load(open(market_path, encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        print(f"FAILED — cannot read marketplace.json: {exc}")
        return 1

    plugins = market.get("plugins", [])
    if not plugins:
        problems.append("marketplace.json lists no plugins")

    print(f"Marketplace: {market.get('name', '?')} — {len(plugins)} plugin(s)\n")
    for p in plugins:
        source = p.get("source", "./")
        na, ns = validate_plugin(source, problems)
        print(f"  • {p.get('name','?'):20} {na} agents, {ns} skills  ({source})")

    if problems:
        print(f"\nFAILED — {len(problems)} problem(s):")
        for pr in problems:
            print(f"  - {pr}")
        return 1
    print("\nAll checks passed ✓")
    return 0


if __name__ == "__main__":
    sys.exit(main())
