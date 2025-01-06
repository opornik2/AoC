#!/usr/bin/env python

import sys

iters = 2000
summ = 0

def mix(x, y): return x ^ y 
def prune(x): return x % 16777216

def calc(s):
    a = prune(mix(s * 64, s))
    b = prune(mix(a // 32, a))
    c = prune(mix(b * 2048, b))
    return c

def price(x):
    return int(str(x)[-1])

with open(sys.argv[1], "r") as FH:
    inp = list(map(int, FH.read().strip().split("\n")))


for secret in inp:
    for _ in range (iters):
        secret = calc(secret)
    summ += secret

print(summ)