#!/usr/bin/env python3

import sys
import re


with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n")

seeds = []
soils = []
ferts = []
water = []
light = []
tempe = []
humid = []
locat = []
s2s = []
s2f = []
f2w = []
w2l = []
l2t = []
t2h = []
h2l = []

def parse (array, line):
    (des, sou, ran) = line.split(" ")
    array.append({"des":int(des), "sou":int(sou), "ran":int(ran)})


def mapping(array, num):
    for r in array:
        s_st = r['sou']
        s_en = r['sou'] + r['ran']
        if num in range(s_st, s_en+1):
            return r['des'] + num - r['sou']
    return num



for line in t:
    print(line)
    match = re.search('^seeds: (.*)',line)
    if match:
        seeds = list(map(int, match.group(1).split(" ")))
        break

mark = False
for line in t:
    if 'to-soil' in line:
        mark = True
        continue
    if not mark: continue
    if line == "": break
    parse(s2s, line)

mark = False
for line in t:
    if 'to-fertilizer' in line:
        mark = True
        continue
    if not mark: continue
    if line == "": break
    parse(s2f, line)

mark = False
for line in t:
    if 'to-water' in line:
        mark = True
        continue
    if not mark: continue
    if line == "": break
    parse(f2w, line)

mark = False
for line in t:
    if 'to-light' in line:
        mark = True
        continue
    if not mark: continue
    if line == "": break
    parse(w2l, line)

mark = False
for line in t:
    if 'to-tempe' in line:
        mark = True
        continue
    if not mark: continue
    if line == "": break
    parse(l2t, line)

mark = False
for line in t:
    if 'to-humidity' in line:
        mark = True
        continue
    if not mark: continue
    if line == "": break
    parse(t2h, line)

mark = False
for line in t:
    if 'to-location' in line:
        mark = True
        continue
    if not mark: continue
    if line == "": break
    parse(h2l, line)


for num in seeds: soils.append(mapping(s2s, num))
for num in soils: ferts.append(mapping(s2f, num))
for num in ferts: water.append(mapping(f2w, num))
for num in water: light.append(mapping(w2l, num))
for num in light: tempe.append(mapping(l2t, num))
for num in tempe: humid.append(mapping(t2h, num))
for num in humid: locat.append(mapping(h2l, num))

print(min(locat))
