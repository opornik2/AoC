#!/usr/bin/env python

import sys

summ = 0
start = 50
m = 100
debug = True if "debug" in sys.argv else False

def log(x):
    if debug:
        print(x)

def counter (s, b):
    global summ, m
    log(f"start={s}, {b} ={s+b}")
    s = s + b
    summ += abs(s) // m
    if s == 0 or s <= -100:
        summ += 1
    if s >= 0:
        s = s % m
    else:
        s = 100 - (s % m)
    log(f"summ = {summ}")
    return s

#####################################################

with open(sys.argv[1], "r") as FH:
    inp = FH.read().strip()

inp2 = inp.replace('R','').replace('L','-')
for el in inp2.split('\n'):
    start = counter(start, int(el))

print(summ)

