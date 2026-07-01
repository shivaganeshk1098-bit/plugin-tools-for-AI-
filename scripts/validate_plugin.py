#!/usr/bin/env python3
"""Validate the agentic-engineer plugin structure.

Checks that the plugin manifests are valid JSON and that every agent and skill
has well-formed frontmatter with the required fields and matching names.

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


def main() -> int:
    problems: list[str] = []

    # 1. Manifests must be valid JSON.
    for manifest in [".claude-plugin/plugin.json", ".claude-plugin/marketplace.json"]:
        path = os.path.join(ROOT, manifest)
        try:
            json.load(open(path, encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            problems.append(f"[manifest] {manifest}: {exc}")

    # 2. Agents: frontmatter with name + description; name must match filename.
    agents_dir = os.path.join(ROOT, "agents")
    agents = sorted(f for f in os.listdir(agents_dir) if f.endswith(".md"))
    for a in agents:
        fm, body = parse_frontmatter(os.path.join(agents_dir, a))
        if fm is None:
            problems.append(f"[agent] {a}: no YAML frontmatter")
            continue
        if not fm.get("name"):
            problems.append(f"[agent] {a}: missing 'name'")
        if not fm.get("description"):
            problems.append(f"[agent] {a}: missing 'description'")
        if fm.get("name") and fm["name"] != a[:-3]:
            problems.append(f"[agent] {a}: name '{fm['name']}' != filename '{a[:-3]}'")
        if len(body.strip()) < 50:
            problems.append(f"[agent] {a}: body too short")

    # 3. Skills: each dir needs SKILL.md with name (matching dir) + description.
    skills_dir = os.path.join(ROOT, "skills")
    skills = sorted(
        d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d))
    )
    for s in skills:
        path = os.path.join(skills_dir, s, "SKILL.md")
        if not os.path.exists(path):
            problems.append(f"[skill] {s}: missing SKILL.md")
            continue
        fm, body = parse_frontmatter(path)
        if fm is None:
            problems.append(f"[skill] {s}: no YAML frontmatter")
            continue
        if not fm.get("name"):
            problems.append(f"[skill] {s}: missing 'name'")
        if not fm.get("description"):
            problems.append(f"[skill] {s}: missing 'description'")
        if fm.get("name") and fm["name"] != s:
            problems.append(f"[skill] {s}: name '{fm['name']}' != directory '{s}'")
        if len(body.strip()) < 50:
            problems.append(f"[skill] {s}: body too short")

    print(f"Agents checked: {len(agents)}")
    print(f"Skills checked: {len(skills)}")
    if problems:
        print(f"\nFAILED — {len(problems)} problem(s):")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("\nAll checks passed ✓")
    return 0


if __name__ == "__main__":
    sys.exit(main())
