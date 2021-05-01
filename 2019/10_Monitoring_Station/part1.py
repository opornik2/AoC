#!/usr/bin/python3

import sys
from math import floor

debug = True
t = [] # pelna lista punktow
met = [] # lista meteorytow
ray = {} # slownik: klucz=meteor, wartosc=set prostych
max_seen = 0
station = []
distance = {}

with open(sys.argv[1], mode='r') as inputfile:
    t = inputfile.read().strip().split('\n')

for x in range(len(t)):
    for y in range(len(t[x])):
        if t[x][y] == '#':
            met.append((x,y))

for p in met:
    ray[p] = set()  #create a set
    min_distance = 10000;
    for r in met:
        if p == r: continue
        input()
        a = 0.0
        b = 0.0
        if debug: print ("p=%s  r=%s" % (p, r))
        # wykres funkcji liniowej  0=ax+b
        if p[1] == r[1]:
            #linia pionowa
            if r[0] < p[0]:
                ray[p].add('up')
            else:
                ray[p].add('down')
        else:
            #linia pozioma lub ukosna
            a = float(p[0]-r[0]) / float(p[1]-r[1])
            b = p[0]-a*p[1]
            distance[(a,b)] = abs(r[0]-p[0]) + abs(r[1]-p[1])
            if debug: print("dist=%i  a=%f  b=%f" %(distance[(a,b)], a, b))
            if r[1] < p[1]:
                #if distance[(a,b)] < min_distance:
                    ray[p].add(('left',a,b))
                    min_distance = distance[(a,b)]
            else:
                #if distance[(a,b)] < min_distance:
                    ray[p].add(('right',a,b))
                    min_distance = distance[(a,b)]
    print("%i - %s" % (len(ray[p]), p))
    if len(ray[p]) > max_seen:
        max_seen = len(ray[p])
        station = p

print(station)
for m in ray[station]:
    print("%s  min. distance: %i" % (m, distance[m]))
sys.exit()

