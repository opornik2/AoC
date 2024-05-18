#!/usr/bin/env python3

import sys

def move(cursor, previous):
    global maxsteps, grid2, visited_crosses
    next_steps = set()
    #print_dic(grid2)
    #print()
    for d in 0+1j, -1, 0-1j, 1:
        try:
            if grid[cursor+d] == '#': continue
            if grid[cursor+d] == '<' and d == 0+1j: continue
            if grid[cursor+d] == '>' and d == 0-1j: continue
            if grid[cursor+d] == 'v' and d == -1: continue
            if grid[cursor+d] == '^' and d == 1: continue
        except: #if key error
            continue

        if cursor+d == previous: continue
        if cursor+d in visited_crosses: 
            grid2 = dict(grid)
            continue
        # found valid direction
        next_steps.add(cursor+d)
    if len(next_steps) > 1:   # we have a crossroads
        visited_crosses.add(cursor)
    for ns in next_steps:
        try:
            if steps[ns] < steps[cursor] + 1:
                steps[ns] = steps[cursor] + 1
            elif steps[ns] >= steps[cursor] + 1:
                grid2 = dict(grid)
                return
        except:
            steps[ns] = steps[cursor] + 1
        grid2[ns] = "O"
        if ns == endpoint:
            if steps[endpoint] > maxsteps:
                maxsteps = steps[endpoint]
            grid2 = dict(grid)
        move(ns, cursor)
    return

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

sys.setrecursionlimit(5000)
grid = grid2cplxdic(t)
grid2 = dict(grid)
visited_crosses = set()
steps = dict()
maxsteps = 0
maxcol = len(t[0])
maxrow = len(t)
startpoint = 0+1j
endpoint = complex(maxrow-1, maxcol-2)

grid2[startpoint] = "O"
steps[startpoint] = 0
steps[endpoint] = 0

move(startpoint, startpoint)
print(steps[endpoint])
pass
