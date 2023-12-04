#!/usr/bin/env python3

import sys
import re


with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n")

summ=0
for line in t:
    print(line)
    match = re.search('Card +(\d+): (.*)',line)
    game = int(match.group(1))
    winning = re.split(r' +', match.group(2).split("|")[0].strip())
    owned = re.split(r' +', match.group(2).split("|")[1].strip())
    points = 0
    for w in winning:
        if w in owned:
            if points==0: points=1
            else: points *= 2
    #print(f"points={points}")
    summ += points
print(summ)
