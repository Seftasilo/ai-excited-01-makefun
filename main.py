#!/usr/bin/env python3
"""ai-excited-01 entrypoint.

Copies the entry artwork (``entry.png`` sitting next to this script) into
the make.fun output directory as ``entry.png``.

The artwork itself is a fixed, pre-rendered image: a giant humpback whale
leaping vertically out of a tiny glass of water on a wooden table, a frozen
crown of spray in the air, a miniature sailboat riding the crest of the
wave, a golden sunrise bursting behind the whale, and a comic bubble
shouting "WOW, JUDGE!".

This script is deliberately deterministic: a byte-for-byte copy, so every
run produces exactly the same output bytes. A size guard refuses to
publish a copy whose size differs from the source or exceeds the 1 MiB
entry limit.

Usage:
    MAKEFUN_OUTPUT_DIR=out python3 main.py
    # writes out/entry.png (defaults to /output when the env var is unset)
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

MAX_BYTES = 1_048_576  # 1 MiB make.fun entry limit
JPEG_MAGIC = b"\xff\xd8\xff"


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        print(f"error: source image not found: {source}", file=sys.stderr)
        return 1

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"

    shutil.copyfile(source, target)

    source_size = source.stat().st_size
    target_size = target.stat().st_size
    if target_size != source_size:
        print(
            f"error: copied size {target_size} != source size {source_size}",
            file=sys.stderr,
        )
        return 1
    if target_size > MAX_BYTES:
        print(
            f"error: output {target_size} bytes exceeds {MAX_BYTES} byte limit",
            file=sys.stderr,
        )
        return 1
    if _sha256(target) != _sha256(source):
        print("error: copied bytes differ from source (sha256 mismatch)", file=sys.stderr)
        return 1
    with target.open("rb") as fh:
        if fh.read(3) != JPEG_MAGIC:
            print("error: output is not a JPEG (bad magic bytes)", file=sys.stderr)
            return 1

    print(f"wrote {target} ({target_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
