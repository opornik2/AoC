#!/usr/bin/env python3

import sys
import re
import numpy as np

gal = []
summ = 0
emlin = []
emcol = []
expand = 1000000

def empty_lines(t, li):
    for y, line in enumerate(t):
        if not '#' in line:
            li.append(y)

def array_transform(X):
    return [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

def find_galaxies(t):
    for y, line in enumerate(t):
        for x, char in enumerate(line):
            if "#" in char: gal.append([x,y])


with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n")

empty_lines(t, emlin)
tt = array_transform(t)
empty_lines(tt, emcol)

find_galaxies(t)
while gal:
    g = gal.pop(0)
    #print(f"galaxy g={g}")
    for h in gal:
        #print(f"galaxy h={h}")
        summ += abs(g[0]-h[0]) + abs(g[1]-h[1])
        for eml in emlin:
            if g[1] < eml < h[1]:
                summ += (expand - 1)
                #print(f"line {eml} expanded")
            elif h[1] < eml < g[1]:
                summ += (expand - 1)
                #print(f"line {eml} expanded")
        for emc in emcol:
            if g[0] < emc < h[0]:
                summ += (expand - 1)
                #print(f"col {emc} expanded")
            elif h[0] < emc < g[0]:
                summ += (expand - 1)
                #print(f"col {emc} expanded")


print(summ)

