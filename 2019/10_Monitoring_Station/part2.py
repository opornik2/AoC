#!/usr/bin/python3

import sys
from math import floor

debug = False
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
        a = 0.0
        #if debug: print ("p=%s  r=%s" % (p, r))
        # wykres funkcji liniowej  0=ax+b
        if p[1] == r[1]:
            #linia pionowa
            if r[0] < p[0]:
                ray[p].add('u')
            else:
                ray[p].add('d')
        else:
            #linia pozioma lub ukosna
            a = float(p[0]-r[0]) / float(p[1]-r[1])
            distance[a] = abs(r[0]-p[0]) + abs(r[1]-p[1])
            #if debug: print("dist=%i  a=%f" %(distance[a], a))
            if r[1] < p[1]:
                ray[p].add(('l',a))
            else:
                ray[p].add(('r',a))
    if debug:
        print("%i - %s" % (len(ray[p]), p))
    if len(ray[p]) > max_seen:
        max_seen = len(ray[p])
        station = p

print("Station at %i, %i" %(station[0], station[1]))  #stacja z najwieksza iloscia widocznych meteorytow

s = station
ray = {}
distance = {}

for m in met:
    if s == m: continue
    #input()
    a = 0.0
    dist = abs(m[0]-s[0]) + abs(m[1]-s[1])
    if debug: print ("m=", m)
    if s[1] == m[1]:   #linia pionowa
        if m[0] < s[0]:
            r = ('u',0)    # up of s
        else:
            r = ('o',0)    # down of s
        if dist < distance.get(r,1000):
            ray[r] = m
            distance[r] = dist
    else:
        #linia pozioma lub ukosna
        a = float(s[0]-m[0]) / float(m[1]-s[1])
        #if debug: print("dist=%i  a=%f" %(distance[a], a))
        if m[1] < s[1]:
            r = ('l',a)    # right of s
        else:
            r = ('r',a)    # left of s

        if dist < distance.get(r,1000):
            ray[r] = m
            distance[r] = dist


# rotate the ray clockwise
count = 1
for r in sorted(ray, reverse=True):
    print(count, r, ray[r])
    if count >= 200:
        print(ray[r][1], ray[r][0])
        break
    count += 1


