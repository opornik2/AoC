#!/usr/bin/env python3
import sys
import networkx as nx
#G.add_node(startpoint, steps=13)   #add new node with attribute
#G.nodes[startpoint]['steps']=13  #node attribute changing
#G.nodes.data()  #display nodes
#G.add_edge(startpoint, endpoint, steps=14 )  #add new edge with attribute
#G.edges[startpoint, endpoint]['steps']=14  #edge attribute changing
#G[startpoint][endpoint]['steps']=14   #also edge attribute changing

debug = True if "debug" in sys.argv else False
recur = 0
grid = dict()
graph = dict() # graph of nodes
maxrow = maxcol = 71 if not "test" in sys.argv[1] else 7
sys.setrecursionlimit(2 * maxrow * maxcol)
startpoint = 0+0j
endpoint = complex(maxrow-1, maxcol-1)


# ----------------------------------------------------
def DFS(cursor):  # Depth First Search (recursive)
    global recur
    recur += 1
    if debug: print(f"recur: {recur}")
    visited.add(cursor)
    for dire in [1j, 1, -1j, -1]:
        try:
            if grid[cursor+dire] == " ":
                G.add_edge(cursor, cursor+dire)
                if cursor+dire not in visited:
                    DFS(cursor+dire)
        except: pass
    recur -= 1

def BFS(cursor):  # Breadth First Search (iteration)
    q = [cursor]
    visited.add(cursor)
    while q:
        cursor = q.pop(0)
        for dire in [1j, 1, -1j, -1]:
            try:
                if grid[cursor+dire] == " " and cursor+dire not in visited:
                    visited.add(cursor+dire)
                    q.append(cursor+dire)
                    G.add_edge(cursor, cursor+dire)
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

############################################################################

with open(sys.argv[1], mode='r') as inp:
    t = inp.read().strip().split("\n")

#create empty grid
for y in range(maxrow):
    for x in range(maxcol):
        grid[complex(x, y)] = " "

grid2 = grid.copy()
# bruteforce method, adding one obstacle at a time anh checking (time 1m 47s)
#fill the grid with obstacles until no path from start to end possible
lowlimit = 1024
highlimit = len(t)-1
for i, line in enumerate(t):
    if i >= lowlimit: break
    x, y = line.split(",")
    grid[complex(int(y), int(x))] = "#"

# bisection method, adding one obstacle at a time anh checking (time 1m 47s)
#fill the grid with obstacles until no path from start to end possible
while highlimit-1 > lowlimit:
    j = (highlimit - lowlimit) // 2 + lowlimit
    grid = grid2.copy()
    for i, line in enumerate(t):
        if i >= j: break
        x, y = line.split(",")
        grid[complex(int(y), int(x))] = "#"
        visited = set()
    G = nx.Graph()
    #DFS(startpoint)
    BFS(startpoint)
    print(f"{i}\t{line}")
    if endpoint in G.nodes: lowlimit = j
    else: highlimit = j
