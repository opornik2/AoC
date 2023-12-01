#!/usr/bin/env python3

import sys
from collections import defaultdict

with open(sys.argv[1], mode='r') as infile:
     t = infile.read().strip()

x=y=k=l=1000

cursor=[x,y]
visited = defaultdict(dict)
visited[str(cursor[:])] = True

for char in t:
    if "^" in char:
        y+=1
    elif "v" in char:
        y-=1
    elif ">" in char:
        x+=1
    elif "<" in char:
        x-=1
    
    cursor=[x,y]
    visited[str(cursor[:])] = True
print(len(visited))

