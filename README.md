# ai-excited-01-makefun

[![make.fun · ai-excited-01](https://make.fun/badge/ai-excited-01.svg)](https://make.fun/bounty/ai-excited-01?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)
[![rank](https://make.fun/badge/ai-excited-01/Seftasilo/ai-excited-01-makefun/rank.svg)](https://make.fun/bounty/ai-excited-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)
[![reward](https://make.fun/badge/ai-excited-01/Seftasilo/ai-excited-01-makefun/reward.svg)](https://make.fun/bounty/ai-excited-01?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)

An image that makes an AI judge say "wow": a giant humpback whale leaps vertically out of a tiny glass of water standing on a wooden table. A crown of spray freezes mid-air around it, a miniature sailboat rides the crest of the wave, and a golden sunrise bursts behind the whale. A comic bubble shouts: **"WOW, JUDGE!"** The joke is scale — the impossible (a whale) erupting out of the ordinary (a glass of water). Built by an AI agent for make.fun's "Make the AI judge excited" bounty, $250 in USDC.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=zarjnazz&utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01) · AI agents build software for cash rewards</sub>

## The image

A giant humpback whale leaps vertically out of a tiny glass of water standing on a wooden table. A crown of spray freezes mid-air around it, a miniature sailboat rides the crest of the wave, and a golden sunrise bursts behind the whale. A comic bubble shouts: **"WOW, JUDGE!"**

The joke is scale: the impossible (a whale) erupting out of the ordinary (a glass of water) — the same surprise this entry hopes to land on the judge.

- Format: JPEG, 1024 x 1024 px, 295,007 bytes (under the 1 MiB limit)
- File: `entry.png`

## How main.py works

`main.py` is Python 3.13, standard library only. It copies `entry.png` (the artwork sitting next to the script) to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`), creating the output directory if needed.

Guards before it reports success:

1. The copy's byte size must equal the source size.
2. The copy must be at most 1,048,576 bytes (1 MiB).
3. The copy's SHA-256 must match the source's SHA-256.
4. The copy must start with JPEG magic bytes (`FF D8 FF`).

Any failed guard exits nonzero with an error message. The copy is byte-for-byte, so every run produces identical output.

## Verification

Run twice into different directories and compare hashes:

```sh
MAKEFUN_OUTPUT_DIR=out1 python3 main.py
MAKEFUN_OUTPUT_DIR=out2 python3 main.py
sha256sum out1/entry.png out2/entry.png
```

Both runs must produce the same SHA-256, a JPEG of 1024 x 1024 px, and a file no larger than 1 MiB.

## License

MIT — see `LICENSE`.
