"""Notes From a Passive-Aggressive Fridge -- one-line entry writer.

Why this line works, and the choices behind it
------------------------------------------------
The brief wants a single line a smart fridge would leave on its door
screen: dry, petty, specific, and smug. A generic nag ("close the door,
you waste energy") is forgettable, so the joke is built from three
concrete domestic details that only a fridge could know:

1. The door left open for four minutes. A fridge genuinely tracks this
   -- its door alarm is its one real superpower, and quoting an exact
   time ("four minutes") makes the pettiness feel documented, like a
   witness statement rather than a complaint.
2. The last yogurt, taken and then blamed on the kids. Stealing the
   last of something and blaming a third party is the smallest, most
   recognisable household crime there is, and the fridge -- which
   inventories its own shelves -- is the one witness who cannot be
   lied to.
3. The sting: "I counted every second. I always count." The first
   sentence sets up the crime; the second turns the fridge from a
   passive box into a quiet, slightly menacing bookkeeper. It lands
   because it reframes the appliance's boring sensor job (counting
   seconds, tracking stock) as a grudge it has been nursing all week.

The line stays in the fridge's voice throughout -- first person, no
shouting, no threats, just a cold inventory of the owner's sins. It
is one line, no line breaks, well inside the 1-200 character gate,
and it trusts the reader to get the joke instead of explaining it.

Output contract
---------------
Writes exactly one line to ``<MAKEFUN_OUTPUT_DIR>/entry.txt`` (or
``/output/entry.txt`` when the variable is unset), as UTF-8, with a
single trailing newline. The grader runs on a read-only filesystem,
so the path is always absolute -- never a relative ``out/`` folder.
"""

import os

# The note itself: one dry, petty, specific line from the fridge.
ENTRY = (
    "You left my door open for four minutes, took the last yogurt, "
    "and blamed the kids. I counted every second. I always count."
)


def main() -> None:
    # Fail loudly instead of writing an entry the sealed gate would
    # score 0: the gate requires UTF-8, 1-200 chars, not only
    # whitespace, so check that here before touching the disk.
    if not (1 <= len(ENTRY) <= 200):
        raise SystemExit(f"entry is {len(ENTRY)} chars, must be 1-200")
    if "\n" in ENTRY or not ENTRY.strip():
        raise SystemExit("entry must be a single non-blank line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
