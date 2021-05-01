#!/usr/bin/python3

import sys

rows = 25
lines = 6
img_size = rows * lines
digit = {}
lays = []

with open('input', mode='r') as inputfile:
	t = inputfile.read().strip()
t = list(map(int, t))
k = 0
lay_size = int(len(t)/(rows*lines))

for i in range(0, 100):
    lays.append(list(t)[k:img_size+k])
    k += img_size

for x in range(0,lines):
    for y in range(0,rows):
        pixel = ''
        n = 0
        for l in lays:
            d = l[x*rows +y]
            #print(l)
            #print("line:%i  col:%i  lay:%i  val:%i" % (x, y, n, d))
            #input()
            n += 1
            if d == 2:
                pixel = ''
            elif d == 1:
                pixel = '@'
                break
            elif d == 0:
                pixel = ' '
                break
        print(pixel, end = '')
    print()
