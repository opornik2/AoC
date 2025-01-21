#!/usr/bin/env python

import sys

locks = []
keys = []

with open(sys.argv[1], "r") as FH:
    inp = FH.read().strip()

inpl = inp.replace(".", "0").replace("#", "1").split("\n\n")

for el in inpl:
    seq = el.replace("\n","")
    num = int(seq, 2)
    if seq[0] == "1": locks.append(num)
    else:  keys.append(num)

print(sum( 1 for l in locks for k in keys if l & k == 0))
        #if ~(l ^ k) % 2**35 == 0: total += 1  # if we would need to match exaclty withput any gaps in lock
