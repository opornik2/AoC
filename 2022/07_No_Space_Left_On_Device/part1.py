#!/usr/bin/env python3

import sys
import re

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split('\n')

sizes = {}
sizes['/'] = 0
path = []

for line in t:
    #print line
    if '$ cd ..' in line:
        path.pop()
    elif '$ cd ' in line:
        d = line.split(' ')[2]
        path.append(d)
    elif '$ ls' in line:
        pass
    else:          # if listing of files/dirs
        (nodesize, nodename) = line.split(' ')
        pathstr = "/".join(path)
        pathstr = pathstr[1:]   #skip first /
        if not 'dir' in nodesize:  # if a file
            pathstr = pathstr + "/" + nodename
            sizes[pathstr] = int(nodesize)
        else:
            pathstr = pathstr + "/" + nodename + "/"
            sizes[pathstr] = 0


for key in sorted(sizes.keys()):
    if key == "/": continue
    if key[-1:] != "/":    #if a file
        dd = re.sub(r'(.*/).*$', r'\1', key)
        while True:
            if dd != "/":
                sizes[dd] += sizes[key]
            dd = re.sub(r'(.*/).*/$', r'\1', dd)
            if dd == "/":
                sizes["/"] += sizes[key]
                break

total = 0
for key in sorted(sizes.keys()):
    if key == "/": continue
    if key[-1:] == "/":    #if a dir
        if sizes[key] < 100000:
            total += sizes[key]


print("total="+str(total))

