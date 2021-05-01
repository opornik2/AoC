#!/usr/bin/env python3

import sys
import networkx as nx

root = 'COM'   #root = COM
G = nx.Graph()

with open('input', mode='r') as input:
    t = input.read().strip().split('\n')

for e in t:
    p,s  = e.split(')')
    G.add_edge(p, s)


#print(list(G.nodes))
#print("\n")
#print(list(G.edges))
#for node in G.successors(root):
#    weight = int(G.nodes[node]['w'])
#    print(node + " " + str(G.nodes[node]['w']))
#    for s in G.successors(node):
#        print("  - " + str(s) + " ("+ str(G.nodes[s]['w'])+")")
#        weight += int(G.nodes[s]['w'])
#    if len(list(G.successors(node))) > 0:
#        #print("total node weight = " + str(weight))
#        print(node + " disk weight = " + str(disk_weight(node)))

print(nx.shortest_path_length(G, source='YOU', target='SAN')-2)
