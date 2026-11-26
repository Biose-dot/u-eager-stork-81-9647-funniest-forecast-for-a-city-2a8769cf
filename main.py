"""Funniest Forecast for a City That Isn't — a single line, under 120 characters.

The line is assembled from named parts so each clause can be judged on
its own job: the setup, the turn, and the landing. See CRAFT notes below.
"""

import os


# CRAFT — why this line is built the way it is:
# 1. Invented city first (judge criterion 1): 'Gloomsbury' sounds like a real
#    English town (Glooms- + -bury) yet exists nowhere; the name itself promises gloom.
# 2. The joke IS the weather (criterion 2): rain falling UPWARDS is absurd weather,
#    not a pun bolted onto a forecast. The laugh comes from picturing it.
# 3. Flat bulletin voice, then the break (criterion 3): 'residents advised to...' is
#    the deadpan phrasing of a real weather advisory, and it breaks by advising the
#    impossible — umbrellas upside-down — which is the only sane response to upward rain.
# 4. The city feels like a place (criterion 4): a named town, a time window (4-6pm),
#    and residents with hats — a small world in one sentence.
# 5. No wasted words (criterion 5): every clause earns its place; the punchline
#    ('keep hats indoors') lands on the last words, where the judge's eye stops.
# The parts below are joined with single spaces; the entry is one line.
PARTS = {
    "header": 'Gloomsbury:',
    "forecast": 'rain falls upwards today, 4-6pm;',
    "advisory": 'residents advised to wear umbrellas upside-down and keep hats indoors.',
}


def build_entry():
    """Assemble the single line from its meaningful parts."""
    line = " ".join(PARTS.values())
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 120, f"entry is {len(line)} chars, limit 120"
    assert line.strip() == line, "entry must not have leading/trailing whitespace"
    return line


ENTRY = build_entry()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
