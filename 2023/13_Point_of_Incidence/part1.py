#!/usr/bin/env python3

import sys
import re

summ = 0
grid = []

def array_transform(X):
    return [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

def find_mirrors(grid, multiplier):
    global summ
    for i, line in enumerate(grid):
        try:
            if grid[i-1] == grid[i]:
                axis = i
                refl = 0
                for j in range(0, min(len(grid)-axis, axis)):
                    try:
                        if grid[axis-j-1] == grid[axis+j]: refl += 1
                    except:
                        pass
                    summ += multiplier*refl
                    print(refl)
                    refl = 0
                print(f"axis={axis}, summ={summ}")
        except: pass
    return

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n\n")

for pattern in t:
    for line in pattern.split("\n"):
        grid.append(list(line))

    find_mirrors(array_transform(grid), 1)
    find_mirrors(grid, 100)

print(summ)

