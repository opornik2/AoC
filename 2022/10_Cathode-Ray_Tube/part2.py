#!/usr/bin/env python3

import sys
from collections import defaultdict

with open(sys.argv[1], mode='r') as infile:
    fi = infile.read().strip().split('\n')

cycle = 0
x = 1  # sprite position +- 1 (0-2)
signals = []

def draw():
    if x-1 <= cycle <= x+1:
        print("*", end='')
    else:
        print(".", end='')

for line in fi:
    try:
        (ins, val) = line.split(" ")
        val = int(val)
    except:
        ins = "noop"
    #first cycle
    draw()
    cycle += 1
    if (cycle) % 40 == 0:
        print("")
        cycle = 0
    if ins == "noop":
        continue
    #second cycle
    draw()
    if ins == "addx":
        cycle +=1
        if (cycle) % 40 == 0:
            print("")
            cycle = 0
        x += val

