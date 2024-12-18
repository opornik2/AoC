#!/usr/bin/env python3
import sys

debug = True
test = True
sys.setrecursionlimit(20000)
recur = 0
total = 0
grid = dict()
steps = dict()
path = list()
graph = dict() # graph of nodes
if test: maxrow = maxcol = 7
else: maxrow = maxcol = 71
startpoint = 0+0j
endpoint = complex(maxrow-1, maxcol-2)
last_crosses = [startpoint]
visited = set()

#potrzebna lista z droga (po kolei odwiedzane punkty) i sprawdzanie czy lista juz istnieje czy nie.
#robimy liste, jak gotowa tworzymy z niej tuple i uzywamy go do hashowania slownika. Wartoscia jest ilosc krokow.

steps[startpoint] = 0
steps[endpoint] = 0

# ----------------------------------------------------

def find_all_paths(cursor):
    global recur, visited
    recur += 1
    #print(f"recurrency {recur}")
    if cursor == endpoint:
        path.append(cursor)
        recur -= 1
        return 1
    if cursor in path:
        path.pop()
        recur -= 1
        return 0
    path.append(cursor)

    for nexttry, length in graph[cursor]:
        if nexttry in path: continue
        if find_all_paths(nexttry):
            paths.add(tuple(path))
            #print(f"added {path}")
        path.pop()
    recur -= 1

def move(cursor, previous):
    path = []
    while True:
        path.append(cursor)
        grid[cursor] = "O"
        possible_directions = set()
        for d in 0+1j, -1, 0-1j, 1:
            try:
                if grid[cursor+d] == '#': continue
            except: #if key error
                continue
            if cursor+d == previous: continue
            # found valid direction
            possible_directions.add(cursor+d)
        pathlen = len(path)
        if len(possible_directions) > 1 or cursor == endpoint or cursor == startpoint:
            return (cursor, previous, pathlen, possible_directions)
        elif len(possible_directions) == 1:
            previous = cursor
            cursor = list(possible_directions)[0]
        else:
            print("ERROR!")
            print(f"cursor {cursor}, prev {previous}, path {path}, possdir {possible_directions}")
            sys.exit(0)

def move_to_next_cross(cursor, previous):
    global grid, path, last_crosses, graph, recur
    recur += 1
    # move to the next crossroad
    cursor, previous, pathlen, possible_directions = move(cursor, previous)
    # we are at crossroad
    #print()
    #print_dic(grid)
    #grid = dict(grid)
    #print(f"last_crosses:{last_crosses}")
    last_cross = last_crosses.pop()
    try:
        for v in graph[last_cross]:
            if v[0] == cursor and v[1] == pathlen: 
                path = [last_cross]  # reset path
                #print(f"path {last_cross} -> {cursor} already visited")
                last_crosses.append(last_cross)
                #print(f"last_crosses:{last_crosses}")
                recur -= 1
                return   # we already added this link
        for v in graph[cursor]:
            if v[0] == last_cross and v[1] == pathlen: 
                path = [last_cross]  # reset path
                #print(f"path {cursor} -> {last_cross} already visited")
                last_crosses.append(last_cross)
                #print(f"last_crosses:{last_crosses}")
                recur -= 1
                return   # we already added this link
    except: pass

    graph.setdefault(last_cross, []).append( (cursor, pathlen) ) #wskazanie na node i dlugosc do niego
    graph.setdefault(cursor, []).append( (last_cross, pathlen) ) #wskazanie na node i dlugosc do niego
    #print(f"added 2 links between {last_cross} and {cursor} lenght {pathlen}")
    last_crosses.append(last_cross)
    last_crosses.append(cursor)
    for ns in possible_directions:
        move_to_next_cross(ns, cursor)

    recur -= 1
    last_cross = last_crosses.pop()
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

############################################################################

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n")

#create empty grid
for y in range(maxrow):
    for x in range(maxcol):
        grid[complex(x, y)] = "."

#fill the grid with obstacles
for line in t:
    x, y = line.split(",")
    grid[complex(int(y), int(x))] = "#"

grid[startpoint] = "O"

move_to_next_cross(startpoint, startpoint)
print("found all crosses")

for k, v in graph.items():
    print(f"{k}:\t{v}")

#traverse graph and find all possible paths from start to end
recur = 0
path = list()
paths = set()
find_all_paths(startpoint)
print(f"found all {len(paths)} paths")


#for each path count its lenght
#print(paths)
summ = 0
for path in paths:
    pathlist = list(path)
    try:
        while pathlist:
            nodea = pathlist.pop(0)
            nodeb = pathlist[0]
            for node, steps in graph[nodea]:
                if node == nodeb:
                    summ += steps
                    break
    except:
        pass
    #print(f"path sum: {summ}")
    if summ > total:
        total = summ
    summ = 0

print("counted all paths")

#print the longest one
print(total)

