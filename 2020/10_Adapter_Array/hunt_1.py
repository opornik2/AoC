#!/usr/bin/python3
# https://hunt.reaktor.com/#tattoo

import sys
import re
import itertools

t = []

def chunks(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))



with open(sys.argv[1], mode='r') as inputfile:
    ch = inputfile.read().strip().split('\n')

for i, el in enumerate(chunks(ch[int(sys.argv[2])], 8)):
    #print("%i %s - %i %s" % (i, el, int(el, 2), chr(int(el, 2))))
    t.append(int(el, 2))

idx = 0
valid = False

while True:
    if t[idx] < 40:
        idx = t[idx]
        valid = True
    elif valid:
        print("%i %s" % (idx, chr(t[idx])))
        sys.exit(0)
    else:
        idx += 1
