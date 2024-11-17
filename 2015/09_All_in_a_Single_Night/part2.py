#!/home/jbloch/AOC/venv/bin/python3

import sys
import networkx as nx
from itertools import permutations

with open(sys.argv[1], mode='r') as infile:
     t = infile.read().strip().split("\n")

G = nx.Graph()

for line in t:
    start = line.split(" to ")[0]
    (end, d) = line.split(" to ")[1].split(" = ")
    G.add_edge(start, end, weight=int(d))  #add new edge with attribute

#print(G.nodes.data())  #display nodes
#print(G.edges.data())  #display nodes
#print("\n\n")

maxdist = 0
maxroute = []
for route in permutations(G.nodes):
    #print(route)
    totaldist = 0
    last = ""
    for el in route:
        if last:
            #print(f"{last} - {el}")
            #print(G.edges[last, el]["weight"])
            totaldist += G.edges[last, el]["weight"]
        last = el
    #print(totaldist)
    #print("\n")
    if totaldist > maxdist:
        maxdist = totaldist
        maxroute = route[::]

print(f"Maximal distance is {maxdist} on {maxroute}")


