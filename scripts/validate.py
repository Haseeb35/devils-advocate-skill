#!/usr/bin/env python3
"""Repository checks for the Devil's Advocate skill.

Validates what `claude plugin validate` does not cover:
  - SKILL.md frontmatter (name matches folder, description present and within limits)
  - version is identical in plugin.json, marketplace.json and the top CHANGELOG entry
  - every eval case is well formed (prompt.md, case.yaml, at least one grader)

Standard library only. Exit code 0 on success, 1 on any failure.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)


def frontmatter(path: Path) -> dict[str, str] | None:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    fields = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip()
    return fields


def check_skills() -> None:
    skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
    if not skills:
        fail("no skills found under skills/")
    for skill in skills:
        rel = skill.relative_to(ROOT)
        fm = frontmatter(skill)
        if fm is None:
            fail(f"{rel}: missing YAML frontmatter")
            continue
        if fm.get("name") != skill.parent.name:
            fail(f"{rel}: name '{fm.get('name')}' does not match folder '{skill.parent.name}'")
        desc = fm.get("description", "")
        if not desc:
            fail(f"{rel}: description is empty")
        elif len(desc) > 1024:
            fail(f"{rel}: description is {len(desc)} chars (max 1024)")
        lines = skill.read_text(encoding="utf-8").count("\n")
        if lines > 500:
            fail(f"{rel}: {lines} lines (keep SKILL.md under 500)")


def check_versions() -> None:
    plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
    market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
    versions = {"plugin.json": plugin.get("version")}
    for entry in market.get("plugins", []):
        if entry.get("name") == plugin.get("name"):
            versions["marketplace.json"] = entry.get("version")
    m = re.search(r"^## \[(\d+\.\d+\.\d+)\]", (ROOT / "CHANGELOG.md").read_text(), re.M)
    versions["CHANGELOG.md"] = m.group(1) if m else None
    if len(set(versions.values())) != 1:
        fail("version mismatch: " + ", ".join(f"{k}={v}" for k, v in versions.items()))


def check_evals() -> None:
    cases = sorted(p for p in (ROOT / "evals").iterdir() if p.is_dir())
    if not cases:
        fail("no eval cases under evals/")
    for case in cases:
        rel = case.relative_to(ROOT)
        prompt = case / "prompt.md"
        if not prompt.exists() or frontmatter(prompt) is None:
            fail(f"{rel}: prompt.md missing or has no settings block")
        yaml = case / "case.yaml"
        if not yaml.exists():
            fail(f"{rel}: case.yaml missing")
        else:
            text = yaml.read_text()
            if not re.search(r'^schema_version: "[\d.]+"$', text, re.M):
                fail(f"{rel}: case.yaml needs a quoted schema_version")
            if not re.search(rf"^name: {re.escape(case.name)}$", text, re.M):
                fail(f"{rel}: case.yaml name does not match folder")
        graders = sorted((case / "graders").glob("*.md"))
        if not graders:
            fail(f"{rel}: no graders")
        for g in graders:
            fm = frontmatter(g)
            if fm is None or "type" not in fm:
                fail(f"{g.relative_to(ROOT)}: grader has no frontmatter with a type")


def main() -> int:
    check_skills()
    check_versions()
    check_evals()
    if errors:
        print("✘ Validation failed:\n" + "\n".join(f"  - {e}" for e in errors))
        return 1
    print("✔ All repository checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
