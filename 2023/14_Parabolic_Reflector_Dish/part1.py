#!/usr/bin/env python3

import sys
import re
import numpy as np

summ = 0

def print_array(a):
    for l in a: print(*l)

def tiltN(grid):
    for line in grid:
        moves = 0
        while True:
            for i in range(1, len(line)):
                if  line[i] == "O":
                    if "." in line[i-1]:
                            line[i-1] = "O"
                            line[i] = "."
                            moves += 1
            if moves == 0: break
            moves = 0

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n")

grid = [list(line) for line in t]
dgrid = np.array(grid)
tgrid = dgrid.transpose()
tiltN(tgrid)
grid = tgrid.transpose()
print_array(grid)
for i, line in enumerate(grid):
    summ += np.count_nonzero(line=="O") * (len(grid) - i)

print(summ)
