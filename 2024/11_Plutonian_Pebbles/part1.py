#!/usr/bin/env python3

import sys

#naive algorith is enough for 25 iterations - extend the list in a loop

#stones = list(map(int, '0 1 10 99 999'.split(" ")))
#stones = list(map(int, '125 17'.split(" ")))
#stones = list(map(int, '3028 78 973951 5146801 5 0 23533 857'.split(" ")))
stones = list(map(int, '0 7 6618216 26481 885 42 202642 8791'.split(" ")))

for blink in range(25):
    newstones = []
    print(f"blink {blink}")
    for v in stones:
        digits = len(str(v))
        if v == 0: newstones.append(1)
        elif digits % 2 == 0:
            half = int(digits/2)
            newstones.append(int(str(v)[0:half]))
            newstones.append(int(str(v)[half:]))
        else: newstones.append(v * 2024)
    stones = newstones[::]

print(len(stones))
