#!/usr/bin/env python3

import sys

with open('input', mode='r') as input:
    t = input.read()

floor=0
for i, e in enumerate(t):
    if e=="(":
        floor += 1
    elif e==")":
        floor -= 1
    else:
        print("Error")
    if floor < 0:
        print(i+1)
        sys.exit()

