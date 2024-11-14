#!/usr/bin/env python3

import sys

steps = steps = int(sys.argv[2]) # 26501365

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

#sys.setrecursionlimit(5000)
with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n")

maxcol = len(t[0])
maxrow = len(t)
visited = set()
grid = grid2cplxdic(t)

#find start
for y, line in enumerate(t):
    if "S" in line:
        startpoint = complex(y, line.index("S"))
        break

grid[startpoint] = "."
visited.add(startpoint)

for _ in range(steps):
    neigh = set()
    for point in visited:
        for i in (-1, 1, 0-1j, 0+1j):
            try:
                if grid[point + i] == ".":
                    neigh.add(point + i)
            except: pass
    #flip state
    for point in neigh:
        if grid[point] == ".":
            grid[point] = "O"
    for point in visited:
        if grid[point] == "O":
            grid[point] = "."
    visited = neigh

print_dic(grid)
print(len(visited))
