#!/usr/bin/env python3

import sys
import re

summ = 0

def print_array(a):
    for l in a: print(*l)

def find_mirror(grid, max_smudges):
    global summ
    seen = []
    grid = ["".join(row) for row in grid]
    for i in range(0,len(grid)-1):
        seen = grid[i::-1]
        rest = grid[i+1:i+1+len(seen)]
        seen = seen[:len(rest)]
        diff = [ 1 for pair in zip(seen, rest) for k in range (0, len(pair[0])) if pair[0][k]!=pair[1][k] ]
        if len(diff) == max_smudges:
            axis = i+1
            print(f"axis={axis}")
            #print_array(reversed(seen))
            #print("---")
            #print_array(rest)
            return axis
    return 0

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n\n")

for pattern in t:
    grid = [line for line in pattern.split("\n")]
    print("by column")
    summ += find_mirror(list(zip(*grid)), 1)
    print("by line")
    summ += find_mirror(grid, 1 ) * 100

print(summ)

