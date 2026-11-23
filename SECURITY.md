# Security Policy

## Scope

This project is a set of instructions for Claude (a Markdown skill), plus plugin manifests and small build scripts. It contains no runtime code that executes on your machine when the skill is used, and it requests no tools beyond what Claude already has.

Relevant reports include:

- Content in `SKILL.md` that could cause Claude to take unexpected actions (for example, run commands or access files it shouldn't)
- Problems in the plugin manifests, release workflow or build scripts that could affect people installing the plugin
- A tampered release asset

## Reporting a vulnerability

Please **do not open a public issue**. Report privately through GitHub:

1. Go to the [Security tab](https://github.com/Haseeb35/devils-advocate-skill/security) of this repository.
2. Click **Report a vulnerability**.

You can expect an acknowledgement within 7 days. Fixes ship as a patch release, and reporters are credited in the changelog unless they prefer otherwise.

## Supported versions

Only the latest release receives fixes.
