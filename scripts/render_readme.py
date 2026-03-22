#!/usr/bin/env python3
"""Regenerate README.md YAML frontmatter from hf.space.toml (run after editing the TOML)."""

from __future__ import annotations

import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
CONFIG = ROOT / "hf.space.toml"


def build_frontmatter(cfg: dict) -> str:
    r = cfg["readme"]
    lines = [
        "---",
        f'title: {r["title"]}',
        f'emoji: {r["emoji"]}',
        f'colorFrom: {r["color_from"]}',
        f'colorTo: {r["color_to"]}',
        f'sdk: {r["sdk"]}',
        f'sdk_version: {r["sdk_version"]}',
        f'python_version: {r["python_version"]}',
        f'app_file: {r["app_file"]}',
        f'pinned: {str(r["pinned"]).lower()}',
        "---",
        "",
        "<!-- Frontmatter above is generated from hf.space.toml via: python scripts/render_readme.py -->",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    with CONFIG.open("rb") as f:
        cfg = tomllib.load(f)

    new_fm = build_frontmatter(cfg)
    text = README.read_text(encoding="utf-8")

    if not text.lstrip().startswith("---"):
        # No frontmatter: prepend generated block
        body = text
        README.write_text(new_fm + body, encoding="utf-8")
    else:
        rest = text.lstrip()[3:].lstrip("\n")
        closing_line = None
        close_pos = None
        for line in rest.splitlines(keepends=True):
            if line.strip() == "---":
                closing_line = line
                close_pos = rest.find(line)
                break
        if close_pos is None or closing_line is None:
            raise SystemExit(f"{README}: no closing --- for frontmatter")
        body = rest[close_pos + len(closing_line) :]
        README.write_text(new_fm + body.lstrip("\n"), encoding="utf-8")

    ns, name = cfg["space"]["namespace"], cfg["space"]["name"]
    print(f"Updated {README.relative_to(ROOT)} (Space: {ns}/{name})")


if __name__ == "__main__":
    main()
