#!/usr/bin/env python3

import sys
t = []
mem = 0

with open('input', mode='r') as input:
    for line in input:
        t = list(map(int, line.split('\t')))
        mem += max(t) - min(t)

print("result = " + str(mem))
sys.exit(0)

