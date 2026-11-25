#!/usr/bin/env python3
"""One Line, Big Laugh — one line, one big laugh.

Writes the single entry line to /output/entry.txt. Deterministic:
same input, same bytes, every run.
"""
import os

ENTRY_TEXT = "I asked the vending machine for a refund and it gave me a second bag of chips instead, so technically we are even."


def write_entry(path="/output/entry.txt"):
    """Write the entry line to path, creating the folder if needed.

    The line is exactly 114 characters, so the file is always
    115 bytes including the trailing newline.
    """
    assert len(ENTRY_TEXT) == 114, "entry line must stay 114 chars"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


def main():
    write_entry()


if __name__ == "__main__":
    main()
