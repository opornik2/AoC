#!/usr/bin/env python3
import sys
import networkx as nx

debug = True if "debug" in sys.argv else False
sys.setrecursionlimit(200000)
recur = 0
grid = dict()
graph = dict() # graph of nodes
maxrow = maxcol = 71 if not "test" in sys.argv[1] else 7
startpoint = 0+0j
endpoint = complex(maxrow-1, maxcol-1)
visited = set()


# ----------------------------------------------------

def DFS(cursor):       # Depth First Search
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

#fill the grid with obstacles
for i, line in enumerate(t):
    if i >= 1024: break
    x, y = line.split(",")
    grid[complex(int(y), int(x))] = "#"

grid[startpoint] = "."
G = nx.Graph()
#G.add_node(startpoint, steps=13)   #add new node with attribute
#G.nodes[startpoint]['steps']=13  #node attribute changing
#G.nodes.data()  #display nodes
#G.add_edge(startpoint, endpoint, steps=14 )  #add new edge with attribute
#G.edges[startpoint, endpoint]['steps']=14  #edge attribute changing
#G[startpoint][endpoint]['steps']=14   #also edge attribute changing

DFS(startpoint)
for node in list(nx.shortest_path(G, source=startpoint, target=endpoint)):
    grid[node] = "."
    #input()
    #print_dic(grid)
if debug: print_dic(grid)
print(nx.shortest_path_length(G, source=startpoint, target=endpoint))
