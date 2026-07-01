# Changelog

All notable changes to this project are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] — Initial release

### Added
- **6 agents**: `architect`, `code-reviewer`, `debugger`, `test-engineer`,
  `refactorer`, `docs-writer` — each scoped to the minimum tools it needs.
- **7 skills**: `plan-feature`, `review-diff`, `write-tests`, `debug-issue`,
  `safe-refactor`, `explain-codebase`, `craft-commit`.
- Plugin manifest and single-plugin marketplace manifest for one-command install.
- README with install/usage instructions and an end-to-end worked example.
- `CONTRIBUTING.md` guide and MIT `LICENSE`.
- Plugin structure validation script (`scripts/validate_plugin.py`) and a
  GitHub Actions workflow that runs it on every push and pull request.
