#!/usr/bin/env python3
"""One-Line Robot Wedding Vows entry generator.

Writes a single line of wedding vows for a robot couple to
/output/entry.txt. Python 3.13 stdlib only, no network, fully
deterministic: the same vow is written on every run.
"""

import os

# The vow: a promise, specific machine detail (co-processor, low
# battery, factory reset), with the joke paying off in the last words.
VOW = (
    "I take you, my lawfully wedded co-processor, to have and to hold, "
    "in sickness and in low battery, till death or factory reset do us "
    "part."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = VOW.strip()
    if not text:
        raise SystemExit("entry is empty")
    if len(text) > 160:
        raise SystemExit(f"entry is {len(text)} characters, over the 160 limit")
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
