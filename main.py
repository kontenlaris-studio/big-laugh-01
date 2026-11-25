#!/usr/bin/env python3
"""One Line, Big Laugh — one line, one big laugh.

Writes the single entry line to /output/entry.txt. Deterministic:
same input, same bytes, every run.
"""
import os

LINE = "I asked the vending machine for a refund and it gave me a second bag of chips instead, so technically we are even."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
