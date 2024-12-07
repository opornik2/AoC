#!/usr/bin/env python3

import sys

def print_dic(a):
    for r in range(0, maxrow):
        for c in range(0, maxcol):
            try:
                print(a[complex(r,c)], end="")
            except:
                print(" ", end="")
        print()

def grid2cplxdic(grid, ignore_chars=""):
    """
    converts traditional [x(column), y(row)] grid into a dic with inverted coordinates
    based on complex numbers:
    returns: row + col j with their value
    0+0j ----> 0+9j
      |          |
      |          |
    9+0j ----> 9+9j
    """
    dic = {}
    ignore = set(ignore_chars)
    for row, line in enumerate(grid):
        for col, char in enumerate(line):
            if char in ignore: continue
            dic[complex(row, col)] = char
    return dic
    # parsing such dic:  for k, v in dic.items()
##########

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n")

grid = grid2cplxdic(t)
maxcol = len(t[0])
maxrow = len(t)
summ = 0
dire = {"slash":[-1+1j, 1-1j], "backslash":[1+1j, -1-1j]}
for k, v in grid.items():
    #print(f"{k}\t{v}")
    if v == "A":
        cnt = 0
        for d, c in dire.items():
            #print(d)
            try:
                if (grid[k+c[0]] == "M" and grid[k+c[1]] == "S") or (grid[k+c[0]] == "S" and grid[k+c[1]] == "M"):
                    cnt += 1
            except:
                pass
        if cnt == 2:
            summ += 1

print(summ)