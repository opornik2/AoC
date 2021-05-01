#!/usr/bin/python3

import sys
import re
import itertools

debug = False
number = 29221323
preamble = []
current = 0

with open(sys.argv[1], mode='r') as inputfile:
    t = inputfile.read().strip().split('\n')

while True:
    summ = 0
    mini = 999999999999
    maxi = 0
    for i in range(current, len(t)):
        q = int(t[i])
        if q < mini: mini = q
        if q > maxi: maxi = q
        summ += int(t[i])
        if summ > number:
            current += 1
            break
        if summ == number:
            print("Hurra")
            print("weakness=" + str(mini + maxi))
            sys.exit(0)



