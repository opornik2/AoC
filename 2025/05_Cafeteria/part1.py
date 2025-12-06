#!/usr/bin/env python3

import sys

with open(sys.argv[1], mode='r') as input:
    (ranges_s, avail_s) = input.read().strip().split('\n\n')

ranges = ranges_s.split("\n")
avail = map(int,avail_s.split("\n"))
total = 0

for ingid in avail:
    for r in ranges:
        (start,end) = r.split("-")
        if ingid in range(int(start), int(end)+1):
            total += 1
            break
print(total)
