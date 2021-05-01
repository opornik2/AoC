#!/usr/bin/python3

import sys

debug = False
with open(sys.argv[1], mode='r') as inputfile:
    t = inputfile.read().strip().split('\n')
for o in t:
    print(o)

long = len(t[0])

x = y = 0
c = 0
while True:
    y = (y+3) % long
    x += 1
    try:
        if t[x][y] == '#': c += 1
    except:
        print(c)
        break
final = c

x = y = 0
c = 0
while True:
    y = (y+1) % long
    x += 1
    try:
        if t[x][y] == '#': c += 1
    except:
        print(c)
        break
final *= c

x = y = 0
c = 0
while True:
    y = (y+5) % long
    x += 1
    try:
        if t[x][y] == '#': c += 1
    except:
        print(c)
        break
final *= c

x = y = 0
c = 0
while True:
    y = (y+7) % long
    x += 1
    try:
        if t[x][y] == '#': c += 1
    except:
        print(c)
        break
final *= c

x = y = 0
c = 0
while True:
    y = (y+1) % long
    x += 2
    try:
        if t[x][y] == '#': c += 1
    except:
        print(c)
        break
final *= c

print(final)

