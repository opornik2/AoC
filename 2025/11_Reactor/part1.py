#!/usr/bin/env python3
import sys
import networkx as nx

debug = True if "debug" in sys.argv else False
sys.setrecursionlimit(200000)
recur = 0
graph = dict() # graph of nodes
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

############################################################################

with open(sys.argv[1], mode='r') as inp:
    t = inp.read().rstrip("\n").split("\n")

G = nx.DiGraph()
for line in t:
    outp = []
    (inp, rest) = line.split(": ")
    outp = rest.split(" ")
    graph[inp] = outp
    for el in outp:
        G.add_edge(inp, el)


#print(G.nodes.data())  #display nodes
#print(G.edges.data())  #display nodes
print(len(list(nx.all_simple_paths(G, "you", "out"))))



#G.add_node(startpoint, steps=13)   #add new node with attribute
#G.nodes[startpoint]['steps']=13  #node attribute changing
#G.nodes.data()  #display nodes
#G.add_edge(startpoint, endpoint, steps=14 )  #add new edge with attribute
#G.edges[startpoint, endpoint]['steps']=14  #edge attribute changing
#G[startpoint][endpoint]['steps']=14   #also edge attribute changing
