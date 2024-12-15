#!/usr/bin/env python3

import sys
from itertools import chain
from collections import defaultdict

debug = 1
summ = 0
dire = [1, -1, 1j, -1j]
visited = set()
plants = list()
areas = list()
area = defaultdict(int)
perim = defaultdict(int)

def find_neib(cursor, plant):
    global visited, recursions
    possible_locations = set()
    if cursor in visited: 
        return
    visited.add(cursor)
    for dire in [-1j, 1j, -1, 1]:
        try:
            if grid[cursor+dire] == plant: 
                possible_locations.add(cursor+dire)
                find_neib(cursor+dire, plant)
        except: pass
    if debug: print(f"{cursor}\t{plant}")
    area[len(plants)-1] += 1
    perim[len(plants)-1] += 4 - len(possible_locations)    #number of borders is 4 minus no. of neib.


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

if debug: print_dic(grid)
for k, v in grid.items():
    if k not in visited:
        plants.append(v)
        find_neib(k, v)


for k in area.keys():
    s = area[k] * perim[k]
    if debug: 
        print(f"plant: {plants[k]}, area={area[k]} * perim={perim[k]} = {s}")
    summ += s
print(summ)