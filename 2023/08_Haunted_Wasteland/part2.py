#!/usr/bin/env python3

import sys
import re
from collections import Counter

step = 0
dic = {}

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n")

path = t.pop(0)
t.pop(0)
for line in t:
    match = re.search("^(\w+) = \((\w+), (\w+)\)", line)
    node, lef, rig = match.groups()
    dic[node] = [lef, rig]

path_l = len(path)
i = 0
nodes = []
for el in dic.keys():
    if 'A' in el[2]: nodes.append(el)

while True:
    zets = len([ el for el in nodes if 'Z' in el[2] ])
    if zets > 2: print(zets)
    if zets == len(nodes): break
    if i == path_l: i = 0
    for k, el in enumerate(nodes):
        if path[i] == 'L':   nodes[k] = dic[el][0]
        elif path[i] == 'R': nodes[k] = dic[el][1]
        else: print("error")
    i += 1
    step += 1

print(step)

