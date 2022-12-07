#!/usr/bin/env python3

import sys
import re

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split('\n')

names = {}
sizes = {}
path = []
tree = {}

for line in t:
    print line
    if '$ cd ..' in line:
        path.pop()
    elif '$ cd ' in line:
        d = line.split(' ')[2]
        path.append(d)
    elif '$ ls' in line:
        pass
    else:
        (nodesize, nodename) = line.split(' ')
        pathstr = "/".join(path)
        if not 'dir' in nodesize:  # a file
            size = int(nodesize)
            sizes[pathstr] += size
        else:                      # a directory
            sizes[pathstr+"/"+nodename] = 0
        names[pathstr].append(nodename)


