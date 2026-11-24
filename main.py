#!/usr/bin/env python3
"""Make the Judge Smile - make.fun entry.

Writes the entry line to /output/entry.txt (UTF-8).
"""
import os

ENTRY = "The bus driver waited while an old man counted out coins in exact change, then waved off the last one and said, keep it, it's your lucky day \u2014 and the whole bus smiled."


def main():
    # Competition gate: entry must be 1-200 characters.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
