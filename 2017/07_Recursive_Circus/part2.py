#!/usr/bin/env python3

import sys
import networkx as nx

root = sys.argv[1]   #root = airlri

def disk_weight(node):
    disk = 0
    if len(list(G.successors(node))) == 0:
        return int(G.nodes[node]['w'])
    else:
        for s in G.successors(node):
            disk += disk_weight(s)
    return disk + int(G.nodes[node]['w'])

G = nx.DiGraph()

with open('input', mode='r') as input:
    t = input.read().strip().split('\n')

for e in t:
    if ' -> ' in e:
        n,con  = e.split(' -> ')
        node, w = n.split(' ')
        weight = w[1:-1]
        for child in con.split(', '):
            G.add_edge(node, child)
    else:
        node, w = e.split(' ')
        weight = w[1:-1]
    G.add_node(node, w=weight)


#print(list(G.nodes))
#print(list(G.edges))
for node in G.successors(root):
#    weight = int(G.nodes[node]['w'])
#    print(node + " " + str(G.nodes[node]['w']))
#    for s in G.successors(node):
#        print("  - " + str(s) + " ("+ str(G.nodes[s]['w'])+")")
#        weight += int(G.nodes[s]['w'])
    if len(list(G.successors(node))) > 0:
        #print("total node weight = " + str(weight))
        print(node + " disk weight = " + str(disk_weight(node)))


