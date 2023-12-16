#!/usr/bin/env python3

import sys
import re
import numpy as np

gal = []
summ = 0

def expand_lines(t):
    addlines = []
    addline = ""
    for y, line in enumerate(t):
        if not '#' in line:
            addlines.append(y)
            addline = line
            print(f"added line {y}")
    for y in reversed(addlines):
        t.insert(y, addline)
    return t

def array_transform(X):
    return [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

def find_galaxies(t):
    for y, line in enumerate(t):
        for x, char in enumerate(line):
            if "#" in char: gal.append([x,y])


with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n")

#expand the universe
tt = expand_lines(t)
t = array_transform(tt)
tt = expand_lines(t)
t = array_transform(tt)
#print(["".join(line) for line in t])

find_galaxies(t)
while gal:
    g = gal.pop(0)
    for h in gal:
        summ += abs(g[0]-h[0]) + abs(g[1]-h[1])

print(summ)

