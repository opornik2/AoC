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
    grid = input.read()

t = grid.split("\n")
maxcol = len(t[0])
maxrow = len(t)
grid = grid2cplxdic(t)
splits = 0

for k, v in grid.items():
    if 'S' in v:
        grid[k] = '|'
    try:
        if '.' in v and '|' in grid[k-1]:
            grid[k] = '|'
    except: pass
    if '^' in v and '|' in grid[k-1]:
        splits += 1
        try: grid[k-1j] = '|'
        except: pass
        try: grid[k+1j] = '|'
        except: pass
    print_dic(grid)

print(splits)
