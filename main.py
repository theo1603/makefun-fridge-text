#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun bounty entry.

Writes the single line a smart fridge texts its owner at 3am to
/output/entry.txt. Python 3 stdlib only, no network, deterministic.

Revision: the first draft ("fridge, not a therapist") leaned on a
well-worn trope. This version is fresher — a machine that has been
awake since 2019 keeping a years-long tally, a specific witness
(the celery), and the punch landing in the last three words.
"""

import os

LINE = (
    "I've been awake since 2019 and I've never once seen you eat "
    "a vegetable at 3am. The celery is judging you. So am I."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 140, f"entry must be 1-140 chars, got {len(text)}"
    assert text and not text.isspace()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
