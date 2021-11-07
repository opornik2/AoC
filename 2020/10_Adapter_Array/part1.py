#!/usr/bin/python3

import sys

diff1 = 0
diff3 = 1

with open(sys.argv[1], mode='r') as inputfile:
    t = inputfile.read().strip().split('\n')

t.append('0')
t = sorted(list(map(int, t)))
i = 0

while True:
    try:
        if t[i+1] - t[i] == 1:
            diff1 += 1
        elif t[i+1] - t[i] == 3:
            diff3 += 1
    except:
        break
    i += 1

print(diff1)
print(diff3)
print(diff1 * diff3)

sys.exit(0)

