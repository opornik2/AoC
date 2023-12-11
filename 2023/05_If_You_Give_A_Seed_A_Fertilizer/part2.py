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


def mapping(rule_arr, in_arr):
    out_arr = []
    while len(in_arr) > 0:
        in_range = in_arr.pop()
        in_start = in_arr.pop()
        in_end = in_start + in_range - 1
        matched = False
        for r in rule_arr:
            # r['sou'], r['ran'], r['des']
            sou_start = r['sou']
            sou_end = r['sou'] + r['ran'] -1
            des_start = r['des']
            if in_start >= sou_start and in_start <= sou_end:
                if in_end <= sou_end:  #caly zakres sie pokrywa
                    out_arr.append(in_start - sou_start + des_start)
                    out_arr.append(in_range)
                    matched = True
                else:
                    out_arr.append(in_start - sou_start + des_start)
                    out_arr.append(sou_end - in_start + 1)
                    in_arr.append(sou_end + 1)
                    in_arr.append(in_range - (sou_end - in_start + 1))
                    matched = True
        if matched == False:
                out_arr.append(in_start)
                out_arr.append(in_range)
    return out_arr

#===========================================================================
#===========================================================================
#===========================================================================


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

soils = mapping(s2s, seeds)
print("\nsoils",soils)
ferts = mapping(s2f, soils)
print("\nferts",ferts)
water = mapping(f2w, ferts)
print("\nwater",water)
light = mapping(w2l, water)
print("\nlight",light)
tempe = mapping(l2t, light)
print("\ntempe",tempe)
humid = mapping(t2h, tempe)
print("\nhumid",humid)
locat = mapping(h2l, humid)
print("\nlocat",locat)

result = [locat[i] for i in range(0, len(locat), 2)]
print(min(result))

