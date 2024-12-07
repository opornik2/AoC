#!/usr/bin/env python3
import sys

def check(l, dir):
    matching = 0
    if dir: r = l[::]
    else:   r = list(reversed(l[::]))
    a = r.pop(0)
    while r:
        try: 
            b = r.pop(0)
        except:
            break
        if a < b and b-a <= 3:
            matching += 1
        else:
            return 0
        a = b
    return matching



with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n")

safe = 0
for line in t:
    rap = line.split(" ")
    rap = [int(el) for el in rap]
    raplen = len(rap)
    #print(rap)
    if rap[0] < rap[len(rap)-1]: dir = True
    else: dir = False
    matching = check(rap, dir)

    if matching == 0:
        for k in range(raplen):
            modrap = rap[::]
            modrap.pop(k)
            matching = check(modrap, dir)
            if matching == len(modrap) -1:
                safe += 1
                break
    elif matching == raplen -1:
        safe += 1
    else:
        print(line)
      
print(safe)