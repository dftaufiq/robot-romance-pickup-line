# Robot Romance: One-Line Pickup Lines for AI — one line, written to /output/entry.txt.
# The line: a robot's dead neurons fire again. Setup (neurons I thought were dead)
# + reveal in the final clause (my ReLU hasn't fired like that since pretraining).
# Deliberately NOT battery/charging/reboot: RULES.txt criterion 3 calls those worn
# moves. Fresh angle: activation functions + pretraining, two ML terms in one breath.
# 93 chars, one line, deterministic: no time, randomness, network or env use.
import os

LINE = "You activated neurons I thought were dead — my ReLU hasn't fired like that since pretraining."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
