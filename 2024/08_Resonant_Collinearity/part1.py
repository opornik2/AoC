#!/usr/bin/env python3

import sys
import itertools

debug = True

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
freq = dict()  #coordinates for each antenna type
antinodes = set()

for k, v in grid.items():
    if v != ".":
        try: freq[v]
        except: freq[v] = set()
        freq[v].add(k)

for k, sites in freq.items():  # check each frequency, v is set of positions
    if debug: print(f"{k}\t{sites}")
    for pair in itertools.permutations(sites, r=2):
        if debug: print(f"{pair}")
        try:
            an = pair[0] + (pair[0] - pair[1])
            grid[an]
            antinodes.add(an)
        except: pass
    
print(len(antinodes))