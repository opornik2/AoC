#!/usr/bin/env python3

import sys

debug = False
blocks = []
summ = 0
blkid = 0
filenum = 0
files = [] #list of indexed dicts [blkid]=, [size]=
gaps = []


# test input
# 2333133121414131402

with open(sys.argv[1], "r") as FH:
    inp = list(map(int, FH.read().strip()))

# create disk image based on the map (input)
#for blocksize in enumerate(inp):
while len(inp)>0:
    try:
        #file
        size = int(inp.pop(0))
        files.append([blkid, size])
        for s in range(size): blocks.append(filenum)
        blkid += size

        #gap
        size = int(inp.pop(0))
        gaps.append([blkid, size])
        for s in range(int(size)): blocks.append(None)
        blkid += size

        filenum +=1
    except: break

# defragment disk
for k, f in enumerate(reversed(files)):
    if debug: print(" ".join(map(str,blocks)).replace("None","."))
    changed = False
    fnum = len(files)-1-k
    fsize = f[1]
    for g in gaps:
        gsize = g[1]
        if fsize <= g[1] and g[0]<=f[0]:   #size <= gap and only to the left blocks
            for i in range(fsize): blocks[f[0]+i] = None   # unreserve space for the file
            f[0] = g[0] #change blkid for file
            if gsize-fsize == 0:
                gaps.remove([g[0],g[1]])
            else:
                g[1] -= fsize #decrease gap size
                g[0] += fsize #move blkid for gap to the right
            for i in range(fsize): blocks[f[0]+i] = fnum   # reserve new space for the file
            changed = True
            break

# count the checksum
for i, v in enumerate(blocks):
    if v != None: summ += i * v

print(summ)
