#!/usr/bin/env python3

import sys
from collections import defaultdict

with open(sys.argv[1], mode='r') as infile:
     t = infile.read().strip()
tt = [el for el in t]
x=y=k=l=1000

cursor=[x,y]
visited = defaultdict(dict)
visited[str(cursor[:])] = True

while tt:
    char = tt.pop(0)
    if "^" in char:
        y+=1
    elif "v" in char:
        y-=1
    elif ">" in char:
        x+=1
    elif "<" in char:
        x-=1
    cursor1=[x,y]
    visited[str(cursor1[:])] = True

    char = tt.pop(0)
    if "^" in char:
        l+=1
    elif "v" in char:
        l-=1
    elif ">" in char:
        k+=1
    elif "<" in char:
        k-=1
    cursor2=[k,l]
    visited[str(cursor2[:])] = True


print(len(visited))

