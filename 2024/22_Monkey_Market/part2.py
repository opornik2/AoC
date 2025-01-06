#!/usr/bin/env python

import sys
from collections import defaultdict

debug = False
iters = 2000 if debug else 2000
seqs = defaultdict(dict)
total = defaultdict(int)
seqprices = defaultdict(set)

def calc(s):
    a = ((s * 64) ^ s) % 16777216
    b = ((a // 32) ^ a) % 16777216
    c = ((b * 2048) ^ b) % 16777216
    return c

with open(sys.argv[1], "r") as FH:
    inp = list(map(int, FH.read().strip().split("\n")))


for line, secret in enumerate(inp):
    prices = []
    changes = []
    price = secret % 10
    prices.append(price)
    if debug: print(f"secret: {secret}")
    sequences = defaultdict(dict)
    seqset = set()
    for _ in range (iters):
        secret = calc(secret)
        price = secret % 10
        changes.append(price - prices[-1])
        prices.append(price)
        try:
            seq = str(changes[-4])+","+str(changes[-3])+","+str(changes[-2])+","+str(changes[-1])
            if debug: print(f"seq: {seq} -> {price}")
            seqset.add(seq)
            if sequences.get(seq, -1) == -1: sequences[seq] = price
            
        except: pass
    seqs[line] = seqset
    seqprices[line] = sequences
    if debug: print("---")

print("Secrets, prices, sequences calculated")

commonseqs = set.union(*seqs.values())

for seq in commonseqs:
    for line, _ in enumerate(inp):
        total[seq] += seqprices[line].get(seq, 0)

print("Total per seq calculated")

total2 = dict()
total2 = sorted(total.items(), key=lambda x:x[1], reverse=True)
print(total2[0], total2[1], total2[2], total2[3], total2[4])
print(max(total.values()))
