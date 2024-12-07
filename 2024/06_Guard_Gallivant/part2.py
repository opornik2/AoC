#!/usr/bin/env python3

import sys

debug = False

def checkbeam(cursor, direction):
    


def go(cursor, direction):
    global visited
    try: visited[cursor]
    except: visited[cursor] = set()
    visited[cursor].add(direction)
    grid[cursor] = "*"
    if debug: print_dic(grid)
    if debug: print(f"{cursor} {direction}")
    if debug: print(f"{visited[cursor]}")
    try:
        if "N" in direction:
            fwd = cursor-1
            i = 0
            while True:
                ontheright = cursor+(i*1j)
                try: 
                    if grid[ontheright] == "#": break  #we reached this direction blocker
                except: break   # we are outside of the grid
                try:
                    if right["N"] in visited[ontheright]:
                        if not fwd in loop:
                            loop.add(fwd)
                            break
                except: pass
                i += 1
            if grid[fwd] == '#': return (cursor, "E")
            else: return (fwd, "N")
        elif "S" in direction:
            fwd = cursor+1
            i = 0
            while True:
                ontheright = cursor-(i*1j)
                try: 
                    if grid[ontheright] == "#": break  #we reached this direction blocker
                except: break   # we are outside of the grid
                try:
                    if right["S"] in visited[ontheright]:
                        if not fwd in loop:
                            loop.add(fwd)
                            break
                except: pass
                i += 1
            if grid[fwd] == '#': return (cursor, "W")
            else: return (fwd, "S")
        elif "E" in direction:
            fwd = cursor+1j
            i = 0
            while True:
                ontheright = cursor+i
                try: 
                    if grid[ontheright] == "#": break  #we reached this direction blocker
                except: break   # we are outside of the grid
                try:
                    if right["E"] in visited[ontheright]:
                        if not fwd in loop:
                            loop.add(fwd)
                            break
                except: pass
                i += 1
            if grid[fwd] == '#': return (cursor, "S")
            else: return (fwd, "E")
        elif "W" in direction:
            fwd = cursor-1j
            i = 0
            while True:
                ontheright = cursor-i
                try: 
                    if grid[ontheright] == "#": break  #we reached this direction blocker
                except: break   # we are outside of the grid
                try:
                    if right["W"] in visited[ontheright]:
                        if not fwd in loop: 
                            loop.add(fwd)
                            break
                except: pass
                i += 1
            if grid[fwd] == '#': return (cursor, "N")
            else: return (fwd, "W")
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
visited = dict()
right = {"N":"E", "E":"S", "S":"W", "W":"N"}
grid = grid2cplxdic(t)
loop = set()

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

for el in loop:
    grid[el] = "O"

print_dic(grid)
print(len(loop))
