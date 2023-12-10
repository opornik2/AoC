#!/usr/bin/env python3

import sys
import re
from collections import Counter
#from igraph import *

summ = 0
dic = {}

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n")

#g = Graph(directed=True)
#g.add_vertices(7)
#Adding the vertex properties
#g.vs["age"] = [25, 31, 18, 47, 22, 23, 50]
#g.vs["gender"] = ["f", "m", "f", "m", "f", "m", "m"]
#Set the edges
#g.add_edges([(0,1), (0,2), (2,3), (3,4), (4,2), (2,5), (5,0), (6,3), (5,6)])
#Set the edge properties
#g.es["is_formal"] = [False, False, True, True, True, False, True, False, False]
#Set different colors based on the gender
#g.vs["label"] = g.vs["name"]
#color_dict = {"m": "blue", "f": "pink"}

path = t.pop(0)
t.pop(0)
for line in t:
    match = re.search("^(\w+) = \((\w+), (\w+)\)", line)
    node, lef, rig = match.groups()
    dic[node] = [lef, rig]

path_l = len(path)
i = 0
node = 'AAA'
while True:
    if node in 'ZZZ': break
    if i == path_l: i = 0
    if path[i] == 'L':
        node = dic[node][0]
    elif path[i] == 'R':
        node = dic[node][1]
    i += 1
    summ += 1

print(summ)

