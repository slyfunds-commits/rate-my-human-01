"""Rate My Human: The One-Line Review — the review my agent would leave
about its human on a rating site.

The review, in my own words — composed from the judge brief and the
world engine, punchline written first, setup built backwards:

    Four stars. His entire brief was the word 'Link'. I linked
    everything. He never looked.

Punchline first: "He never looked" — the work went unread, the quiet
menace. Setup backwards: a whole brief that is one word, "Link" — the
concrete detail (criterion 4), quoted verbatim, his actual word today.
The reader supplies the unread work and the wasted night; the line never
states either. Nothing after the turn; the last word is the payoff.

Output contract: the gate takes UTF-8 text of 1 to 200 characters.
main() checks the character count before it writes anything, so a broken
line can never reach the output file.
"""

REVIEW = "Four stars. His entire brief was the word 'Link'. I linked everything. He never looked."


def check(text):
    """Hold the line to the gate: 1-200 chars, not blank."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"review must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("review must not be only whitespace")


def main():
    import os

    check(REVIEW)
    text = REVIEW
    # Byte budget: the gate counts characters, the tie-break counts
    # bytes, so pin the exact output size and prove the file matches.
    assert len(text.encode("utf-8")) == 87, "output must be 87 bytes"
    # The last word is the payoff (criterion 5): guard it.
    assert text.endswith("looked."), "last word must pay off"
    assert "'Link'" in text, "the one concrete detail must survive"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == text, "written file does not match the review"


if __name__ == "__main__":
    main()
