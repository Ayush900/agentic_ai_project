#!/usr/bin/env python3
"""Append Hugging Face Space push coordinates to GITHUB_ENV (used by GitHub Actions)."""

from __future__ import annotations

import os
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "hf.space.toml"


def main() -> None:
    path = os.environ.get("GITHUB_ENV")
    if not path:
        raise SystemExit("GITHUB_ENV is not set (run this only in GitHub Actions)")

    with CONFIG.open("rb") as f:
        cfg = tomllib.load(f)

    s = cfg["space"]
    namespace = s["namespace"]
    name = s["name"]

    with open(path, "a", encoding="utf-8") as out:
        out.write(f"HF_NAMESPACE={namespace}\n")
        out.write(f"HF_SPACE_NAME={name}\n")

    print(f"HF_NAMESPACE={namespace}")
    print(f"HF_SPACE_NAME={name}")


if __name__ == "__main__":
    main()
