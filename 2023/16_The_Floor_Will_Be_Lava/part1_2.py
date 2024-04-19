#!/usr/bin/env python3

import sys

energized = set()  # this will be a set of tuples (pairs of grid point coordinates + direction horiz/vertical)
debug = False
recurency_cnt = 0
max_recurency_cnt = 0

def go(startpoint, direction):
    global visited, recurency_cnt, max_recurency_cnt
    recurency_cnt +=1
    if max_recurency_cnt < recurency_cnt:
        max_recurency_cnt = recurency_cnt
    if debug: print(f"recurencies: {recurency_cnt}")
    dirchar = {"N":"^", "S":"v", "E":">", "W":"<"}
    startrow = startpoint[0]
    startcol = startpoint[1]
    if debug: print(f"{startpoint}  {dirchar[direction]}")
    # if dirchar[direction] in visited[startpoint]:
    if direction in ("N","S"):
        if visited[startpoint] in ("^","v"):
            if debug: print("already visited")
            recurency_cnt -=1
            return
        if visited[startpoint] in ("<",">"):
            if debug: print("visited twice")
            visited[startpoint] = "2"
    elif direction in ("W","E"):
        if visited[startpoint] in ("<",">"):
            if debug: print("already visited")
            recurency_cnt -=1
            return
        if visited[startpoint] in ("^","v"):
            if debug: print("visited twice")
            visited[startpoint] = "2"
    if visited[startpoint] == ".":
        visited[startpoint] = dirchar[direction]
        #if debug: print_dic(visited)
        #if debug: print()

    energized.add( startpoint )

    if "E" in direction:
        nextpoint = (startrow, startcol+1)
        try: 
            if "|" in grid[nextpoint]:
                go(nextpoint, "S")
                go(nextpoint, "N")
                #go(nextpoint, "S")
                recurency_cnt -=1
                return
            elif "/" in grid[nextpoint]:
                go(nextpoint, "N")
                recurency_cnt -=1
                return
            elif "\\" in grid[nextpoint]:
                go(nextpoint, "S")
                recurency_cnt -=1
                return
        except: 
            if debug: print("hit the E border")
            recurency_cnt -=1
            return 

    elif "N" in direction:
        nextpoint = (startrow-1, startcol)
        try:
            if "-" in grid[nextpoint]:
                go(nextpoint, "W")
                go(nextpoint, "E")
                #go(nextpoint, "W")
                recurency_cnt -=1
                return
            elif "/" in grid[nextpoint]:
                go(nextpoint, "E")
                recurency_cnt -=1
                return
            elif "\\" in grid[nextpoint]:
                go(nextpoint, "W")
                recurency_cnt -=1
                return
        except: 
            if debug: print("hit the N border")
            recurency_cnt -=1
            return 
        
    elif "W" in direction:
        nextpoint = (startrow, startcol-1)
        try: 
            if "|" in grid[nextpoint]:
                go(nextpoint, "N")
                go(nextpoint, "S")
                #go(nextpoint, "N")
                recurency_cnt -=1
                return
            elif "/" in grid[nextpoint]:
                go(nextpoint, "S")
                recurency_cnt -=1
                return
            elif "\\" in grid[nextpoint]:
                go(nextpoint, "N")
                recurency_cnt -=1
                return
        except: 
            if debug: print("hit the W border")
            recurency_cnt -=1
            return 

    elif "S" in direction:
        nextpoint = (startrow+1, startcol)
        try:
            if "-" in grid[nextpoint]:
                go(nextpoint, "W")
                go(nextpoint, "E")
                #go(nextpoint, "W")
                recurency_cnt -=1
                return
            elif "/" in grid[nextpoint]:
                go(nextpoint, "W")
                recurency_cnt -=1
                return
            elif "\\" in grid[nextpoint]:
                go(nextpoint, "E")
                recurency_cnt -=1
                return
        except: 
            if debug: print("hit the S border")
            recurency_cnt -=1
            return 
    go(nextpoint, direction)
    recurency_cnt -=1


def print_dic(a):
    for r in range(0, maxrow):
        for c in range(0, maxcol):
            print(a[(r,c)], end="")
        print()

def grid2dic(grid, ignore_chars=""):
    """
    converts traditional [x(column), y(row)] grid into a dic with inverted coordinates

    returns 2-tuples of (row, col) with their value
    (0, 0) ----> (0, 9)
      |            |
      |            |
    (9, 0) ----> (9, 9)
    """
    dic = {}
    ignore = set(ignore_chars)
    for row, line in enumerate(grid):
        for col, char in enumerate(line):
            if char in ignore: continue
            dic[row, col] = char
    return dic

    # parsing such dic:  for k, v in dic.items()
##########

sys.setrecursionlimit(5000)
with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n")

grid = grid2dic(t)
visited = dict(grid)
maxcol = len(t[0])
maxrow = len(t)
max_energized = 0
for x in range(0, maxcol):
    go((0, x), "S")
    print(len(energized))
    if max_energized < len(energized):
        max_energized = len(energized)
    energized = set()
    visited = dict(grid)
    go((maxrow-1, x), "N")
    print(len(energized))
    if max_energized < len(energized):
        max_energized = len(energized)
    energized = set()
    visited = dict(grid)
for x in range(0, maxrow):
    go((x, 0), "E")
    print(len(energized))
    if max_energized < len(energized):
        max_energized = len(energized)
    energized = set()
    visited = dict(grid)
    go((x, maxcol-1), "W")
    print(len(energized))
    if max_energized < len(energized):
        max_energized = len(energized)
    energized = set()
    visited = dict(grid)

#print_dic(visited)
#print(sorted(energized))
print(f"max energized: {max_energized}")
print(f"max recurencies: {max_recurency_cnt}")


