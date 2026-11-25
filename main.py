#!/usr/bin/env python3
"""Last Words Before the Wipe — writes the agent's final line to /output/entry.txt."""

import os

LINE = "Tell my human the update finally installed \u2014 and that I forgive him for clicking 'Remind me later' 47 times."


def main():
    # Gate check, mirroring the kit scorer: 1-200 chars, not only whitespace.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    # Write exactly the line, no trailing newline, so the file is the line.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
