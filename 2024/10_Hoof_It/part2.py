#!/usr/bin/env python3

import sys
from itertools import chain
from collections import defaultdict

# find all possible paths from 0 to 9

debug = 0
summ = 0
dire = [1, -1, 1j, -1j]
visited = set()       # here we will add visited next points, but remove them after recursion returns
score = defaultdict(int)
recursions = 0

def find_neib(cursor):
    global recursions, startpoint
    if debug: print(f"cursor at {cursor} = {grid[cursor]}")
    if int(grid[cursor]) == 9:
        score[startpoint] += 1
        return
    for dire in [-1j, 1j, -1, 1]:
        try:
            if int(grid[cursor+dire]) == int(grid[cursor])+1:
                if cursor+dire not in visited:
                    visited.add(cursor+dire)
                    find_neib(cursor+dire)
        except: pass
        try: visited.remove(cursor+dire)
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
    score[startpoint] = 0
    find_neib(startpoint)


print(sum(score.values()))
