#!/usr/bin/env python

import sys
from collections import defaultdict
import itertools

lan = defaultdict(set)

with open(sys.argv[1], "r") as FH:
    inp = FH.read().strip().split("\n")

for l in inp:
    a, b = l.split("-")
    lan[a].add(b)
    lan[b].add(a)

tt = [ k for k,v in lan.items() if k[0] == "t" ]

tri = []
summ = 0
for t in sorted(tt):
    for (a, b) in itertools.combinations(lan[t], 2):
        if a in lan[b] and {t, a, b} not in tri: 
            print(f"{t}\t{a}\t{b}")
            tri.append({t, a, b})
            summ += 1

print(summ)