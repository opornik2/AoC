#!/usr/bin/env python3
import sys
import networkx as nx
import copy

debug = True if "debug" in sys.argv else False
graph = dict() # graph of nodes
visited = set()
recur = 0
allpaths = []
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

def modDFS(src, dst, path):  # modified Depth First Search (recursive) to search for all possible paths
    global recur, visited
    if debug: print(f"node: {src}\trecur: {recur}")
    if src == dst:
        allpaths.append(copy.deepcopy(path))
        if debug: print(f"new path: {path}")
    else:
        recur += 1
        for edge in G.edges(src):
            (_, neib) = edge
            path.append(neib)
            #if debug: print(2*recur*"| "+f"{src} -> {neib}")
            modDFS(neib, dst, path)
            path.pop()
        recur -= 1

##########


############################################################################

with open(sys.argv[1], mode='r') as inp:
    t = inp.read().rstrip("\n").split("\n")

G = nx.DiGraph()

with open(sys.argv[1], mode='r') as input:
    grid = input.read().rstrip("\n")

t = grid.split("\n")
maxcol = len(t[0])-1
maxrow = len(t)-1
grid = grid2cplxdic(t)
endnodes = []
total = 0

# create Directed Graph, add nodes and edges
for k, v in grid.items():
    if 'S' in v:
        startnode = k
        grid[k] = '|'
        G.add_node(k)
        continue
    if k.real == 0: continue
    if k.real == maxrow: endnodes.append(k)
    if '|' in grid[k-1]:
        if '.' in v or '|' in v:
            grid[k] = '|'
            G.add_edge(k-1, k)

        elif '^' in v:
            G.remove_node(k-1)
            try:
                grid[k-1j] = '|'
                G.add_edge(k-2, k-1j)
            except: pass
            try:
                grid[k+1j] = '|'
                G.add_edge(k-2, k+1j)
            except: pass
    #print_dic(grid)

print_dic(grid)
modDFS(startnode, 141+2j, [startnode])
#[print(el[0]) for el in G.nodes.data()]  #display nodes
#[print(el) for el in G.edges.data()]  #display nodes
sys.exit()

for endnode in endnodes:
    allpaths = []
    modDFS(startnode, endnode, [startnode])
    if debug: print("\n")
    pathsnum = len(allpaths)
    print(pathsnum)
    total += pathsnum

print(total)
#print(len([p for p in nx.all_simple_paths(G, "svr", "out", cutoff) if "dac" in p and "fft" in p]))
#print(paths)


#G.add_node(startpoint, steps=13)   #add new node with attribute
#G.nodes[startpoint]['steps']=13  #node attribute changing
#G.nodes.data()  #display nodes
#G.add_edge(startpoint, endpoint, steps=14 )  #add new edge with attribute
#G.edges[startpoint, endpoint]['steps']=14  #edge attribute changing
#G[startpoint][endpoint]['steps']=14   #also edge attribute changing
