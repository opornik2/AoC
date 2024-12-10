#!/usr/bin/env python3

import sys

debug = False
right = {-1: 1j, 1: -1j, 1j: 1, -1j: -1}   #dict of right turns from each direction
dirchar = {-1: "^", 1: "v", 1j: ">", -1j: "<"}

visited = set()
blockers = set()


def checkloop(cursor, direction):    #direction is numerical: N=-1, S=1, E=1j, W=-1j
    global right
    loopvisited = set()
    loopgrid = grid.copy()
    while True:
        loopgrid[cursor] = "X"
        if (cursor, direction) in visited: 
            if debug: print_dic(loopgrid)
            return True
        if (cursor, direction) in loopvisited:
            if debug: print_dic(loopgrid)
            return True
        loopvisited.add( (cursor, direction) )
        try:    
            if grid[cursor + direction] == "#":
                direction = right[direction]
            else:
                cursor += direction
        except: return False   #we are out of grid so no loop
        
        

def go(cursor, direction):      #direction is numerical: N=-1, S=1, E=1j, W=-1j
    visited.add( (cursor, direction) )
    visited.add(cursor)
    grid[cursor] = dirchar[direction]
    if debug: print_dic(grid)
    if debug: print(f"{cursor} {direction}")
    try:
        if grid[cursor + direction] == '#': return (cursor, right[direction])
        else: 
            if not cursor+direction in visited and checkloop(cursor, right[direction]):
                if debug: print_dic(grid)
                blockers.add(cursor + direction)
            return (cursor + direction, direction)
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

#sys.setrecursionlimit(5000)
with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n")

maxcol = len(t[0])
maxrow = len(t)

grid = grid2cplxdic(t)

#find start
for k, v in grid.items():
    if v == "^":
        cursor = k
        break

grid[cursor] = "^"
#direction is numerical: N=-1, S=1, E=1j, W=-1j
direction = -1      # -1 so we start to North
while True:
    (cursor, direction) = go(cursor, direction)
    if direction == None:
        break

for el in blockers:
    grid[el] = "O"

print_dic(grid)
print(len(blockers))
