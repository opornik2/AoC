#!/usr/bin/env python3

import sys

def move(cursor, previous):
    global maxsteps, grid2, path, paths, total, last_crosses, nodes, recur
    recur += 1
    print(f"entered recurrency {recur}")
    print(f"I am at {cursor}")
    print(f"the path is {path}")
    grid2[cursor] = "O"
    path.append(cursor)
    possible_directions = set()
    for d in 0+1j, -1, 0-1j, 1:
        try:
            if grid[cursor+d] == '#': continue
        except: #if key error
            continue
        if cursor+d == previous: continue
        # found valid direction
        possible_directions.add(cursor+d)
    pathlen = len(path)-1
    if len(possible_directions) > 1 or cursor == endpoint:   # we have a crossroad
        print()
        print_dic(grid2)
        grid2 = dict(grid)
        print(f"last_crosses:{last_crosses}")
        last_cross = last_crosses.pop()
        try:
            for v in nodes[last_cross]:
                if v[0] == cursor and v[1] == pathlen: 
                    path = [last_cross]  # reset path
                    print(f"path {last_cross} -> {cursor} already visited")
                    last_crosses.append(last_cross)
                    print(f"last_crosses:{last_crosses}")
                    recur -= 1
                    return   # we already added this link
            for v in nodes[cursor]:
                if v[0] == last_cross and v[1] == pathlen: 
                    path = [last_cross]  # reset path
                    print(f"path {cursor} -> {last_cross} already visited")
                    last_crosses.append(last_cross)
                    print(f"last_crosses:{last_crosses}")
                    recur -= 1
                    return   # we already added this link
        except: pass

        nodes.setdefault(last_cross, []).append( (cursor, pathlen) ) #wskazanie na node i dlugosc do niego
        nodes.setdefault(cursor, []).append( (last_cross, pathlen) ) #wskazanie na node i dlugosc do niego
        print(f"added 2 links between {last_cross} and {cursor} lenght {pathlen}")
        path = [cursor]  # start new path
        last_crosses.append(last_cross)
        last_crosses.append(cursor)
    for ns in possible_directions:
        #if ns == endpoint:
        #    path = []
        #    nodes.setdefault(last_cross, []).append( (ns, 1) ) #wskazanie na node i dlugosc do niego
        #    nodes.setdefault(ns, []).append( (last_cross, 1) ) #wskazanie na node i dlugosc do niego
        #    print(f"added 2 links between {last_cross} and {cursor}")
        #    continue
        move(ns, cursor)

    recur -= 1
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

sys.setrecursionlimit(20000)
recur = 0
grid = grid2cplxdic(t)
grid2 = dict(grid)
total = 0
steps = dict()
path = list()
paths = dict() # dict of paths (tuples created from lists)
nodes = dict()
maxsteps = 0
maxcol = len(t[0])
maxrow = len(t)
startpoint = 0+1j
last_crosses = [startpoint]
endpoint = complex(maxrow-1, maxcol-2)

#potrzebna lista z droga (po kolei odwiedzane punkty) i sprawdzanie czy lista juz istnieje czy nie.
#robimy liste, jak gotowa tworzymy z niej tuple i uzywamy go do hashowania slownika. Wartoscia jest ilosc krokow.

grid2[startpoint] = "O"
steps[startpoint] = 0
steps[endpoint] = 0

move(startpoint, startpoint)

#traverse nodes for the longest path
total = 0
for k, v in nodes.items():
    print(f"{k}: {v}")

#while True:

pass
