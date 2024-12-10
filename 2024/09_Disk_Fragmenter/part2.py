#!/usr/bin/env python3

import sys

blocks = []
summ = 0
fileid = 0
filesizes = []
gapsizes = []


# test input
# 2333133121414131402

with open(sys.argv[1], "r") as FH:
    inp = FH.read().strip()

# create disk image based on the map (input)
for block, size in enumerate(inp):
    if block % 2 == 0:
        filesizes.append(int(size))
        for s in range(int(size)):
            blocks.append(fileid)
    else:
        gapsizes.append(int(size))
        for s in range(int(size)):
            blocks.append(None)
        fileid += 1

# defragment disk
files = len(filesizes)-1
for i, fsize in enumerate(reversed(filesizes)):
    for j, gapsize in enumerate(gapsizes):
        if fsize <= gapsize:
            pass
    pass

# count the checksum
for i, v in enumerate(blocks):
    summ += i * v

print(summ)
