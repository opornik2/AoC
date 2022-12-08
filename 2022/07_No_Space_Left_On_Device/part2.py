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
        pathstr = pathstr[1:]   #remove first /
        if not 'dir' in nodesize:  # if a file
            pathstr = pathstr + "/" + nodename
            sizes[pathstr] = int(nodesize)
        else:
            pathstr = pathstr + "/" + nodename + "/"
            sizes[pathstr] = 0

for key in sorted(sizes.keys()):
    if key == "/": continue
    #print("file="+key+"   size="+str(sizes[key]))
    if key[-1:] != "/":    #if a file
        dd = re.sub(r'(.*/).*$', r'\1', key)
        while True:
            #print("dd="+dd)
            if dd != "/":
                sizes[dd] += sizes[key]
            dd = re.sub(r'(.*/).*/$', r'\1', dd)
            if dd == "/":
                #print("old root size="+str(sizes["/"]))
                sizes["/"] += sizes[key]
                #print("new root size="+str(sizes["/"]))
                break

left = 70000000 - sizes["/"]
need = 30000000 - left
smallest = 70000000
print("need="+str(need))

for key in sorted(sizes.keys()):
    if key == "/":
        print("dir="+key+"   size="+str(sizes[key]))
        continue
    if key[-1:] == "/":    #if a dir
        print("dir="+key+"   size="+str(sizes[key]))
        if sizes[key] > need and smallest > sizes[key]:
            smallest = sizes[key]


print(smallest)
