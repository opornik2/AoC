#!/usr/bin/python3

import sys

rows = 25
lines = 6
img_size = rows * lines
digit = {}
lays = []

with open('input', mode='r') as input:
	t = input.read().strip()
t = list(map(int, t))
k = 0
for i in range(0,100):
    lays.append(list(t)[k:img_size+k])
    k += img_size

for l in lays:
    while len(l) > 0:
        d = l.pop(0)
        digit[d] = digit.get(d, 0) + 1
    print("0:%i  1:%i  2:%i  multiply:%i" % (digit[0], digit[1], digit[2], digit[1]*digit[2]))
    digit = {}

