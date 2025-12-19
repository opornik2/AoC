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


def modDFS(src, dst, path):  # modified Depth First Search (recursive) to search for all possible paths
    global recur, visited
    #if debug: print(f"recur: {recur}")
    if src == dst:
        allpaths.append(copy.deepcopy(path))
    else:
        recur += 1
        for edge in G.edges(src):
            (_, neib) = edge
            path.append(neib)
            if debug: print(2*recur*"| "+f"{src} -> {neib}")
            modDFS(neib, dst, path)
            path.pop()
        recur -= 1

##########
#         I
#        / \
#        G H
#        |X|
#        L M
#        \ /
#         O
############################################################################


G = nx.DiGraph()
G.add_edge("I", "G")
G.add_edge("I", "H")
G.add_edge("G", "L")
G.add_edge("G", "M")
G.add_edge("L", "O")
G.add_edge("H", "L")
G.add_edge("H", "M")
G.add_edge("M", "O")

splits = 0
endnodes = []
total = 0

modDFS("I", "O", [])
print(allpaths)
