#!/usr/bin/env python3

import sys
#from itertools import chain
from collections import defaultdict

debug = True
test = True
grid = dict()
summ = 0
dires = [1, 1j , -1, -1j]
if test: maxrow = maxcol = 7
else: maxrow = maxcol = 71
recursions = 0
startpoint = 0+0j
endpoint = complex(maxcol-1, maxrow-1)
path = 0
paths = []
visited = defaultdict(set)
steps = defaultdict(int)

def find_neib(cursor):
    global recursions, path
    if cursor in visited[path]: 
        steps[path] -= 1
        return
    visited[path].add(cursor)
    steps[path] += 1
    grid[cursor] = "O"
    if debug: print_dic(grid)
    if cursor == endpoint:
        paths.append(steps[path])
        return
    for dire in dires:
        try:
            if grid[cursor+dire] != "#":
                if cursor+dire not in visited[path]:
                    find_neib(cursor+dire)
        except: pass   # if out of grid
    #steps[path] -= 1
    grid[cursor] = ","


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

#create empty grid
for y in range(maxrow):
    for x in range(maxcol):
        grid[complex(x, y)] = "."

#fill the grid with obstacles
for line in t:
    x, y = line.split(",")
    grid[complex(int(y), int(x))] = "#"

basegrid = grid.copy()

if debug: print_dic(grid)

find_neib(startpoint)
