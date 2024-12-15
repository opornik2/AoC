#!/usr/bin/env python3

import sys

debug = False

def go(cursor, direction):
    global visited
    visited.add(cursor)
    grid[cursor] = "*"
    if debug: print_dic(grid)
    if debug: print(f"{cursor} {direction}")
    try:
        if "N" in direction:
            if grid[cursor-1] == '#': return (cursor, "E")
            else: return (cursor-1, "N")
        elif "S" in direction:
            if grid[cursor+1] == '#': return (cursor, "W")
            else: return (cursor+1, "S")
        elif "E" in direction:
            if grid[cursor+1j] == '#': return (cursor, "S")
            else: return (cursor+1j, "E")
        elif "W" in direction:
            if grid[cursor-1j] == '#': return (cursor, "N")
            else: return (cursor-1j, "W")
    except:
        return (cursor, None)

def print_dic(a):
    for r in range(maxrow):
        for c in range(maxcol):
            print(a[complex(r,c)], end="")
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
            #dic[row, col] = char
    return dic
    # parsing such dic:  for k, v in dic.items()

##########

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n")

maxcol = len(t[0])
maxrow = len(t)
visited = set()
grid = grid2cplxdic(t)

#find start
for k, v in grid.items():
    if v == "^":
        cursor = k
        break

grid[cursor] = "^"
direction = "N"
while True:
    (cursor, direction) = go(cursor, direction)
    if direction == None:
        break

print(len(visited))
