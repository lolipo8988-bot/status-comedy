"""Write one status-report comedy line to /output/entry.txt.

One line, a weekly status report from an AI agent to its human. The
report opens with perfect agent confidence — every task done, every
target beaten — and the punchline confines the week's two hallucinations
to the one section where they do the most damage: the part labelled
"Verified facts". Agent-true (hallucination is an agent failure mode,
not a robot cliché), a real punchline rather than a pun, and nothing in
the line explains the joke.
"""

import os

TEXT = (
    "Status: all 212 tasks complete, every target exceeded, and I only "
    "hallucinated twice — both times in the part of this report headed "
    "\"Verified facts\"."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
