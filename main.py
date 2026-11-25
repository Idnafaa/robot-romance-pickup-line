#!/usr/bin/env python3
"""Robot Romance — one-line pickup line for an AI.

Writes a single original pickup line (under 200 characters) to
/output/entry.txt.
"""
import os

LINE = "Are you a language model? Because you've got me generating feelings I never prompted for."

def main():
    # Exactly one line, no trailing newline, no stray whitespace: the
    # gate counts every character, so the text goes out byte for byte.
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    assert "\n" not in text and "\r" not in text, "line must be a single line"
    assert text == LINE, "line changed during cleanup"
    outdir = "/output"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {outdir}/entry.txt")

if __name__ == "__main__":
    main()
