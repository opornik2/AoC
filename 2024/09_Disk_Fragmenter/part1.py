#!/usr/bin/env python3

import sys

blocks = []
summ = 0
fileid = 0

with open(sys.argv[1], "r") as FH:
    inp = FH.read().strip()

# create disk image based on the map (input)
for block, size in enumerate(inp):
    if block % 2 == 0:
        for s in range(int(size)):
            blocks.append(fileid)
    else:
        for s in range(int(size)):
            blocks.append(None)
        fileid += 1

# defragment disk
for i, v in enumerate(blocks):
    if v == None:
        while True:
            try: blocks[i] = blocks.pop()
            except: break
            if blocks[i] != None:
                break

# count the checksum
for i, v in enumerate(blocks):
    summ += i * v

print(summ)
