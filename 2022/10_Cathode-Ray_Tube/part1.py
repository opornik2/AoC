#!/usr/bin/env python3

import sys
from collections import defaultdict

with open(sys.argv[1], mode='r') as infile:
    fi = infile.read().strip().split('\n')

cycle = 0
x = 1
signals = []

for line in fi:
    print (line)
    try: 
        (ins, val) = line.split(" ")
        val = int(val)
    except:
        ins = "noop"
    cycle += 1
    if (cycle+20) % 40 == 0:
        signals.append(cycle * x)
        print("=========================")
        print(f"1st cycle={cycle} x={x}")

    #second cycle
    if ins == "addx":
        cycle +=1
        if (cycle+20) % 40 == 0:
            signals.append(cycle * x)
            print("=========================")
            print(f"2nd cycle={cycle} x={x}")
        x += val
    else: continue

print(signals)
summ = 0
for s in signals:
    summ += s
print(summ)

