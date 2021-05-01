#!/usr/bin/python3

import sys
import re
import itertools

debug = False
size = 25
preamble = []
current = 0

with open(sys.argv[1], mode='r') as inputfile:
    t = inputfile.read().strip().split('\n')

for i in range(size, len(t)):
    preamble = t[i-size:i]
    sums = {}
    for co in itertools.combinations(preamble, 2):
        s = int(co[0]) + int(co[1])
        if s not in sums:
            sums[s] = True
    if int(t[i]) in sums:
            continue
    print(t[i])
    sys.exit(0)


