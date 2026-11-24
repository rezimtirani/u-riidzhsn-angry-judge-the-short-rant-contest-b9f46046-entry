"""Angry Judge: The Short Rant Contest.

Writes one short rant to $MAKEFUN_OUTPUT_DIR/entry.txt: a funny
rant about the office printer, which only ever jams on the one
document that matters. Standard library only.
"""

import os

RANT = (
    "The printer has never once jammed on a document nobody needed. "
    "It waits, patient and fully inked, until the one page that "
    "decides your morning, then eats it, blinks orange, and prints "
    "a perfect test page nobody asked for — as if to say: I could "
    "do it. I just chose not to."
)


def check_rant(text):
    """Check the rant against the competition gate before writing it.

    The gate needs UTF-8 text of 1 to 400 characters, not only white
    space: one short, funny rant about a small everyday annoyance.
    Returns the cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("rant must not be only whitespace")
    if len(cleaned) > 400:
        raise ValueError("rant is %d characters, over the 400 limit" % len(cleaned))
    return cleaned


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_rant(RANT)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
