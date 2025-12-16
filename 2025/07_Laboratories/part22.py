#!/usr/bin/env python3
import sys
import networkx as nx

debug = True if "debug" in sys.argv else False
graph = dict() # graph of nodes
visited = set()

# ----------------------------------------------------

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


############################################################################

with open(sys.argv[1], mode='r') as inp:
    t = inp.read().rstrip("\n").split("\n")

G = nx.DiGraph()

with open(sys.argv[1], mode='r') as input:
    grid = input.read().rstrip("\n")

t = grid.split("\n")
maxcol = len(t[0])
maxrow = len(t)
grid = grid2cplxdic(t)
splits = 0
endnodes = []
total = 0

for k, v in grid.items():
    if 'S' in v:
        startnode = k
        grid[k] = '|'
        G.add_node(k)
    try:
        if '.' in v and '|' in grid[k-1]:
            grid[k] = '|'
            G.add_edge(k-1, k)
            if k.real == maxrow-1:
                endnodes.append(k)
    except: pass
    if '^' in v and '|' in grid[k-1]:
        splits += 1
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

grid2 = dict(grid)
print_dic(grid)
#print(G.nodes.data())  #display nodes
#print(G.edges.data())  #display nodes
for path in nx.all_simple_paths(G, startnode, 15+6j):
    grid = dict(grid2)
    for n in path:
        grid[n] = "#"
    print(path)
    print_dic(grid)
    print("\n\n")



sys.exit()
for endnode in endnodes:
    print(len(list(nx.all_simple_paths(G, startnode, endnode))))
    total += len(list(nx.all_simple_paths(G, startnode, endnode)))

print(total)
#print(len([p for p in nx.all_simple_paths(G, "svr", "out", cutoff) if "dac" in p and "fft" in p]))
#print(paths)


#G.add_node(startpoint, steps=13)   #add new node with attribute
#G.nodes[startpoint]['steps']=13  #node attribute changing
#G.nodes.data()  #display nodes
#G.add_edge(startpoint, endpoint, steps=14 )  #add new edge with attribute
#G.edges[startpoint, endpoint]['steps']=14  #edge attribute changing
#G[startpoint][endpoint]['steps']=14   #also edge attribute changing
