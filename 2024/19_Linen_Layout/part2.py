#!/usr/bin/env python

import sys
from collections import defaultdict

debug = 0
matched = {}
possible = []
ways = defaultdict(int)

with open(sys.argv[1], "r") as FH:
    inp = FH.read().strip()

(towels_s, designs_s) = inp.split("\n\n")
towels = towels_s.split(", ")
towels.sort(key=len)
maxtowel = len(towels[-1])
designs = designs_s.split("\n")

for design in designs:
    if debug: print(design)
    possible.append(design)
    matching = []
    firststart = start = 0
    length = 1
    while firststart <= maxtowel:
        start = firststart
        while start < len(design):
            matched = False
            while length <= maxtowel:  # check for all lengths from 1 to maxtowel
                frag = design[start:start+length]
                if frag in towels: 
                    matching.append(frag)
                    start += len(frag)
                    length = 1
                    matched = True
                    break
                length += 1
            if not matched:   # if not matched any next towel, lets get back one towel and try again with longer length
                try:
                    start -= len(matching[-1])
                    length = len(matching[-1])+1
                    matching.pop()   # remove last matching towel and try again
                except:
                    break
        if matched:
            ways[design] += 1
        firststart += 1
        length = 1
        matching = []


