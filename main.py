#!/usr/bin/env python3
"""Writes the one word for the whole internet to /output/entry.txt.

Buffering: always loading, always almost there, forever a spinner
away from the thing you actually came for. The alternatives were
Unsubscribe, Cookies and Doomscrolling; Buffering is the one state
everyone online has shared.

Deterministic: the same bytes on every run, no input, no network.
"""
import os

WORD = "Buffering"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
