#!/usr/bin/env python3

import sys
import re

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split(",")

summ = 0
for y, step in enumerate(t):
    hash = 0
    for char in step:
        hash += ord(char)
        hash *= 17
        hash %= 256
    print(f"{y}\t{step}\t{hash}")
    summ += hash

print(summ)
