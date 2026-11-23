# Changelog

All notable changes to this project are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- Eval results comparing the skill against plain Claude (`evals/RESULTS.md`).
- "Why not just ask Claude?" comparison in the README, backed by a recorded side-by-side run.
- Real Deep-mode example.
- `SECURITY.md`, `CODE_OF_CONDUCT.md`, private vulnerability reporting and GitHub Discussions.

## [1.0.0] - 2026-11-23

### Added
- **Standard mode**: the case against, three failure modes with likelihood, warning sign and prevention, the case for, and a verdict.
- **Quick mode**: a five-line gut check for small decisions.
- **Deep mode**: hidden assumptions, five failure modes, a pre-mortem narrative and kill criteria for high-stakes decisions.
- **Compare mode**: critiques each option side by side and picks one.
- Claude Code plugin and marketplace manifests for one-command installation.
- Ready-to-upload `devils-advocate.zip` for Claude.ai, attached to each release.
- Eval suite of six cases runnable with `claude plugin eval`.
- CI that validates the skill, manifests and eval cases on every push.
- Examples recorded from real runs.

[1.0.0]: https://github.com/Haseeb35/devils-advocate-skill/releases/tag/v1.0.0
