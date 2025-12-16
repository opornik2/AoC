#!/usr/bin/env python3
import sys
import networkx as nx

debug = True if "debug" in sys.argv else False
sys.setrecursionlimit(200000)
recur = 0
graph = dict() # graph of nodes
visited = set()

# ----------------------------------------------------

def DFS(node, node2):  # Depth First Search (recursive)
    global recur, visited, dac, fft
    recur += 1
    #if debug: print(f"recur: {recur}")
    visited.add(node)
    for edge in G.edges(node):
        (_, neib) = edge
        if debug: print(2*recur*"| "+f"{node} -> {neib}")
        if "dac" in neib:
            dac += 1
            print(" ############### found DAC ###############")
        if "fft" in neib:
            fft += 1
            print(" ############### found FFT ###############")
        if debug and node2 in neib:
            print(f" =============== reached {node2} ===========\n")
        if neib not in visited:
            DFS(neib, node2)
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

cutoff = 15
#print(G.edges.data())  #display nodes
dac = 0
fft = 0
#DFS(sys.argv[2], "out")
print(f"there are {len(list(G.nodes()))} nodes")
skip = []
for snode in G.nodes():
    dac = 0
    fft = 0
    visited = set()
    DFS(snode, "out")
    if dac == 0 and fft == 0:
        print(snode)
        skip.append(snode)

#sys.exit()

#skip.remove("fft")
#skip.remove("dac")

for node in skip:
    G.remove_node(node)
print(G.nodes.data())  #display nodes

print(f"there are {len(list(G.nodes()))} nodes")
#print(len([p for p in nx.all_simple_paths(G, "svr", "out", cutoff) if "dac" in p and "fft" in p]))
#print(len(list(nx.all_simple_paths(G, "dac", "out", cutoff))))  # = 7314
#print(len(list(nx.all_simple_paths(G, "fft", "dac", cutoff))))  # inf
#print(len(list(nx.all_simple_paths(G, "fft", "out", cutoff))))  # inf
print(len(list(nx.all_simple_paths(G, "svr", "out"))))  # inf
#print(paths)


#G.add_node(startpoint, steps=13)   #add new node with attribute
#G.nodes[startpoint]['steps']=13  #node attribute changing
#G.nodes.data()  #display nodes
#G.add_edge(startpoint, endpoint, steps=14 )  #add new edge with attribute
#G.edges[startpoint, endpoint]['steps']=14  #edge attribute changing
#G[startpoint][endpoint]['steps']=14   #also edge attribute changing
