#!/usr/bin/env python3
import sys
from collections import defaultdict

debug = True if "debug" in sys.argv else False
graph = dict() # graph of nodes
visited = set()
recur = 0
allpaths = []
pathnum = 0
# ----------------------------------------------------

def print_dic(a):
    for r in range(maxrow+1):
        for c in range(maxcol+1):
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


############################################################################

with open(sys.argv[1], mode='r') as inp:
    grid = inp.read().rstrip("\n")

t = grid.split("\n")
maxcol = len(t[0])-1
maxrow = len(t)-1
grid = grid2cplxdic(t)
endnodes = []
total = 0
val = defaultdict(int)

# create Directed Graph, add nodes and edges
for k, v in grid.items():
    if 'S' in v:
        startnode = k
        grid[k] = '|'
        val[k] = 1
        continue
    if k.real == 0: continue
    if k.real == maxrow: endnodes.append(k)
    if '|' in grid[k-1]:
        if '.' in v or '|' in v:
            grid[k] = '|'
            val[k] += val[k-1]

        elif '^' in v:
            try:
                grid[k-1j] = '|'
                val[k-1j] += val[k-1]
            except: pass
            try:
                grid[k+1j] = '|'
                val[k+1j] += val[k-1]
            except: pass
        else:
            print("something wrong happended!!")
            sys.exit(1)
    #print_dic(grid)

print_dic(grid)
for endnode in endnodes:
    total += val[endnode]

print(total)