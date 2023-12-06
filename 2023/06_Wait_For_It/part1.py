#!/usr/bin/env python3

import sys
import re

#time = [7, 15, 30]
#dist = [9, 40, 200]
time = [40,     81,     77,     72]
dist = [219,   1012,   1365,   1089]
records = []

for i, t in enumerate(time):
    longer = 0
    for k in range (1, int(t/2)+1):
        # k^2 - kt - dist = 0  is a quadratic formula
        if k*(t-k) > dist[i]:
            if k==(t-k): longer += 1
            else: longer += 2
            #print(f"{i} - {k}*{t-k}={k*(t-k)} - {longer}")
    records.append(longer)

record=1
for i, n in enumerate(time):
    record *= records[i]
print(record)

