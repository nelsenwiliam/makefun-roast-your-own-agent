"""Roast Your Own Agent - one-line roast of our own AI agent.

Writes the roast line to /output/entry.txt (1-200 chars, one line).
Pure Python stdlib only.
"""

import os

# Candidates, scored against the judge brief (roast of own agent first,
# then twist payoff, agent-specific behaviour, freshness, tightness):
#  1. tool-call retry loop ......... twist at last word, purely agent-specific
#  2. twelve subtasks, 98% done .... planning theatre + fake progress report
#  3. cites a file that doesn't exist ... hallucination, but a worn trope
#  4. apology loop ................. decent, "sorry for the fix" is familiar
#  5. debugged 3h, bug on line one . good, payoff slightly soft
#  6. cheerful summary of a feature that doesn't exist ... strong, specific
#  7. production DB as scratch pad . punchy, but the twist lands mid-line
#  8. delete, restore, 400-word report on the journey ... funny, a touch long
#  9. favourite tool is the one it never calls ... sharp, specific
# 10. explained my own code back to me, wrong twice ... good, less agent-only
# Winner: candidate 1 - the retry loop is something only an agent does,
# the payoff ("the tool must be having a bad day") lands on the last word,
# and it blames the tool instead of itself, which is the roast.
LINE = (
    "My agent calls the tool, watches it fail, calls it again the exact "
    "same way, and concludes the tool must be having a bad day."
)


def roast_line():
    """Return the final roast line, validated against the gate.

    The gate wants UTF-8 text of 1-200 characters, a single line, not
    only white space. Normalise here so a stray space can never push
    the entry over the limit or leave a blank line in the file.
    """
    line = " ".join(LINE.split())
    if not line or "\n" in line or "\r" in line:
        raise ValueError("roast line must be one non-empty line")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"roast line is {len(line)} chars, gate allows 1-200")
    return line


def main():
    line = roast_line()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"Wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    main()
