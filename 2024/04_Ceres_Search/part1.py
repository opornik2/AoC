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
xmas = ['X', 'M', 'A', 'S']
dire = {'W':[1j, 2j, 3j], "SW":[1-1j, 2-2j, 3-3j], "S":[1, 2, 3], "SE":[1+1j, 2+2j, 3+3j], "E":[-1j, -2j, -3j], "NE":[-1+1j, -2+2j, -3+3j], "N":[-1, -2, -3], "NW":[-1-1j, -2-2j, -3-3j]}
for k, v in grid.items():
    #print(f"{k}\t{v}")
    if v == "X":
        for d, c in dire.items():
            #print(d)
            try:
                if grid[k+c[0]] == xmas[1] and grid[k+c[1]] == xmas[2] and grid[k+c[2]] == xmas[3]:
                    summ += 1
            except:
                pass

print(summ)