#!/usr/bin/env python3

import sys
from collections import defaultdict

# naive algorith runs up to around 40 iterations - need recursion?
# NO!  (2024-12-18)
# after reading https://advent-of-code.xavd.id/writeups/2024/day/11/
# the best is to keep stones in dictionary where value is number of stanes same type

#inp = list(map(int, '0 1 10 99 999'.split(" ")))
#inp = list(map(int, '125 17'.split(" ")))
#stones = list(map(int, '3028 78 973951 5146801 5 0 23533 857'.split(" ")))
inp = list(map(int, '0 7 6618216 26481 885 42 202642 8791'.split(" ")))
#inp = [0, 23] # > [1 2 3] > [2024 4048 6072] > [20 24 40 48 60 72]

stones = defaultdict(int)

def splitting():
    for stone, count in stones.items():
        digits = len(str(stone))
        if stone == 0:
            new_stones[1] += count
        elif digits % 2 == 0:
            half = digits // 2
            stone1 = int(str(stone)[0:half])
            stone2 = int(str(stone)[half:])
            new_stones[stone1] += count
            new_stones[stone2] += count
        else:
            new_stones[stone * 2024] = count

for s in inp:
    stones[s] += 1

for _ in range(75):
    new_stones = defaultdict(int)
    splitting()
    stones = new_stones


print(sum(stones.values()))
