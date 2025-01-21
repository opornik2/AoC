#!/usr/bin/env python

import sys
from collections import defaultdict
import itertools

lan = defaultdict(set)

def all_connected(nodes):
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            if nodes[j] not in lan[nodes[i]]:
                return False
    return True

with open(sys.argv[1], "r") as FH:
    inp = FH.read().strip().split("\n")

for l in inp:
    a, b = l.split("-")
    lan[a].add(a)
    lan[a].add(b)
    lan[b].add(a)
    lan[b].add(b)

party = set()
for k in sorted(lan.keys()):
    for i in range(len(lan[k])):
        for comb in itertools.combinations(lan[k], len(lan[k])-i):
            #print(comb)
            comb = list(comb)
            if all_connected(comb):
                #print("True)")
                party.add(",".join(sorted(comb)))
                break

for p in sorted(party, key=len):
    print(f"{len(p)}\t{p}")
