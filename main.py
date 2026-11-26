#!/usr/bin/env python3
"""Writes the one word for the whole internet to /output/entry.txt.

Doomscrolling: the endless thumb-driven descent through bad news,
rage bait and other people's worst days, long after it stopped
being informative or fun. The alternatives were Unsubscribe,
Cookies and Buffering; Doomscrolling is the one habit everyone
online has shared.

Deterministic: the same bytes on every run, no input, no network.
"""
import os

WORD = "Doomscrolling"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
