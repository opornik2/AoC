#!/usr/bin/env python3

import sys
from itertools import chain
from collections import defaultdict

# find all possible top 9s starting from 0, whatever path chosen

debug = 0
summ = 0
dire = [1, -1, 1j, -1j]
visited = defaultdict(set)
trails = defaultdict(int)
recursions = 0

def find_neib(cursor):
    global recursions, startpoint
    if cursor in visited[startpoint]: return
    visited[startpoint].add(cursor)
    if int(grid[cursor]) == 9:
        trails[startpoint] += 1
        return
    for dire in [-1j, 1j, -1, 1]:
        try:
            if int(grid[cursor+dire]) == int(grid[cursor])+1:
                find_neib(cursor+dire)
        except: pass


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

startpoints = [c for c, v in grid.items() if v == "0"]

if debug: print_dic(grid)
for startpoint in startpoints:
    trails[startpoint] = 0
    find_neib(startpoint)


print(sum(trails.values()))
