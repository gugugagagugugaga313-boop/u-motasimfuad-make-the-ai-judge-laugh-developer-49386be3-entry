import os

# One fixed line, written verbatim every run: no randomness, no network,
# no clock, so two runs are byte-identical.
LINE = "Prod didn't break because of my code \u2014 the agent followed AGENTS.md perfectly, and AGENTS.md was the bug."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
