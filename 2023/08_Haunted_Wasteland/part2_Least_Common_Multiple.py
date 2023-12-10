#!/usr/bin/env python3

import sys
import re
from collections import Counter
from math import lcm

dic = {}
nodes = []

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n")

path = t.pop(0)
t.pop(0)
for line in t:
    match = re.search("^(\w+) = \((\w+), (\w+)\)", line)
    node, lef, rig = match.groups()
    dic[node] = [lef, rig]

for el in dic.keys():
    if 'A' in el[2]: nodes.append(el)

step = []
for k, el in enumerate(nodes):
    path_l = len(path)
    i = 0
    node = el
    step.append(0)
    while True:
        if 'Z' in node[2]: break
        if i == path_l: i = 0
        if path[i] == 'L':   node = dic[node][0]
        elif path[i] == 'R': node = dic[node][1]
        i += 1
        step[k] += 1

    print(f"node {k} = steps {step[k]}")

# no idea how to convert list of integers to integers here, so entered them directly :)
print(lcm(16043, 20777, 13939, 18673, 11309, 17621))

