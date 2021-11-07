#!/usr/bin/python3

import sys

diff1 = 0
ciag = [] #ciag kolejnych liczb
iloczyn = 1

with open(sys.argv[1], mode='r') as inputfile:
    t = inputfile.read().strip().split('\n')

t.append('0')
t = sorted(list(map(int, t)))
t.append(max(t)+3)
print(t)

i = 0
while True:
    try:
        if t[i+1] - t[i] == 1:
            diff1 += 1
        else:
            if diff1 == 2: ciag.append(2)   # 3 liczby daja 2 kombinacje
            elif diff1 == 3: ciag.append(4) # 4 liczby daja 4 kombinacje
            elif diff1 == 4: ciag.append(7) # 5 liczb daje 7 kombinacji
            diff1 = 0
    except:
        break
    i += 1

print(ciag)

for el in ciag:
    iloczyn *= el
print(iloczyn)
