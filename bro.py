#!/usr/bin/env python3
"""bro - a friendly CLI companion."""

import random
import sys

BRO_PHRASES = [
    "bro, you got this!",
    "bro, that's fire!",
    "bro, let's goooo!",
    "bro, respect. fr.",
    "bro, you're absolutely crushing it.",
    "bro, no cap, that's impressive.",
    "bro, W moment right there.",
    "bro, you're built different.",
]

def main():
    name = "bro"
    if len(sys.argv) > 1:
        name = sys.argv[1]

    phrase = random.choice(BRO_PHRASES)
    print(f"{name}, {phrase}")

if __name__ == "__main__":
    main()
