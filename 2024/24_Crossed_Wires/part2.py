#!/usr/bin/env python

import sys
from collections import defaultdict
import itertools
import re

wire = defaultdict()
x = defaultdict()
y = defaultdict()
z = defaultdict()
xin = yin = 0
maxz = 0
result = 0

#def andgate(a,b): return a & b
andgate = lambda a,b: a & b
#def orgate(a,b):  return a | b
orgate = lambda a,b: a | b
#def xorgate(a,b): return a ^ b
xorgate = lambda a,b: a ^ b

with open(sys.argv[1], "r") as FH:
    inp = FH.read().strip().split("\n\n")

wires = inp[0].split("\n")
for w in wires:
    k, v = w.split(": ")
    wire[k] = int(v)

for k, v in wire.items():
    if "x" in k:   xin += int(v) * 2**int(k.replace("x",""))
    elif "y" in k: yin += int(v) * 2**int(k.replace("y",""))
zcorrect = xin + yin
print(f"x={xin}\ty={yin}\tcorrect z={zcorrect} / {bin(zcorrect)}")


gatelist = inp[1].split("\n")
for line in gatelist:
    if "z" in line:
        match = re.search(r'z(\d+)', line)
        if maxz < int(match.group(1)): maxz = int(match.group(1))


while True:
    missing = False
    for line in gatelist:
        ab,c = line.split(" -> ")
        a, op, b = ab.split(" ")
        try:
            if op == "AND": wire[c] = andgate(wire[a], wire[b]) 
            elif op == "OR": wire[c] = orgate(wire[a], wire[b])
            elif op == "XOR": wire[c] = xorgate(wire[a], wire[b])
            if "z" in c:
                z[int(c.replace("z",""))] = wire[c]
        except:
            missing = True
    try: 
        [ z[i] for i in range(maxz+1) ]
        break
    except: pass

for k, v in z.items():
    result += v * 2**k
print(result)
