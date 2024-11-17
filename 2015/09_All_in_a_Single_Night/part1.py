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

mindist = 10000
minroute = []
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
    if totaldist < mindist:
        mindist = totaldist
        minroute = route[::]

print(f"Minimal distance is {mindist} on {minroute}")



#nx.all_simple_edge_paths(G, source, target)
#nx.all_pairs_dijkstra_path_length(G, weight='dist'):
#for el in nx.approximation.traveling_salesman_problem(G, weight='weight', cycle=False):
#    print(el)

#route = nx.approximation.christofides(G, weight='dist')
#route = nx.approximation.greedy_tsp(G, weight='dist')
#route =  nx.approximation.traveling_salesman_problem(G, weight='weight', cycle=False)
#route.pop()
#print(nx.approximation.greedy_tsp(G, weight='dist'))

print("This should calculate the same but runs some cities more times, do not know why...")
print(nx.approximation.traveling_salesman_problem(G, weight='weight', cycle=False))


#for el in nx.all_pairs_all_shortest_paths(G, weight='dist'):
#    print(el)


#G.add_node(startpoint, steps=13)   #add new node with attribute
#G.nodes[startpoint]['steps']=13  #node attribute changing
#G.nodes.data()  #display nodes
#G.edges.data()  #display edge
#G.add_edge(startpoint, endpoint, steps=14 )  #add new edge with attribute
#G.edges[startpoint, endpoint]['steps']=14  #edge attribute changing
#G[startpoint][endpoint]['steps']=14   #also edge attribute changing

