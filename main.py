"""Funniest forecast for a city that isn't — one line, max 120 chars.

The entry is a fake weather bulletin for Gloomsbury, a town that does not
exist, where the rain falls upwards. The humour comes from the bulletin
staying deadpan while advising the impossible: umbrellas upside-down,
hats tied to heads.
"""

import os

# The forecast, in the order a bulletin would read it:
#   1. the town,  2. the weather,  3. the advice to residents.
# The punchline lands on a physical gag — hats tied to heads — instead
# of a shrug, because a reader pictures an action, not a mood.
SEGMENTS = [
    "Gloomsbury:",
    "upward rain today, 4-6pm;",
    "residents advised to wear umbrellas upside-down and tie hats to their heads.",
]

MAX_CHARS = 120


def build_entry():
    """Join the bulletin segments into the single entry line."""
    line = " ".join(SEGMENTS)
    if "\n" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, limit {MAX_CHARS}")
    if line != line.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    return line


ENTRY = build_entry()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
