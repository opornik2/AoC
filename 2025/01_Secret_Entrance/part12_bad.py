#!/usr/bin/env python

import sys

zeros = 0
start = 50
m = 100
debug = 1 if "debug" in sys.argv else 0

def log(x):
    if debug:
        print(x)

def counter (s, r):
    global zeros, m
    log(f"start={s}, rotates={r}, end={s+r} -> {(s+r)%m}")
    end = s + r
    if r > 0:
        zeros += abs(end) // m
    else:
        if abs(r) > s:
            if s > 0:
                zeros += 1 + abs(end) // m
            else:
                zeros += abs(r) // m
    if end == 0:
        zeros += 1
    log(f"zeros = {zeros}")
    return end % m

#####################################################

with open(sys.argv[1], "r") as FH:
    inp = FH.read().strip()

inp2 = inp.replace('R','').replace('L','-')
for el in inp2.split('\n'):
    start = counter(start, int(el))

print(zeros)

