#!/usr/bin/env python3

import sys

#naive algorith runs up to around 40 iterations - need recursion?

#stones = list(map(int, '0 1 10 99 999'.split(" ")))
#inp = list(map(int, '125 17'.split(" ")))
#stones = list(map(int, '3028 78 973951 5146801 5 0 23533 857'.split(" ")))
inp = list(map(int, '0 7 6618216 26481 885 42 202642 8791'.split(" ")))
#inp = [0, 23] # > [1 2 3] > [2024 4048 6072] > [20 24 40 48 60 72]
#silnia= 1 > 2 > 6 > 24

print(sys.setrecursionlimit(50))

def parse_stones(stones1, iteration):
    print(f"blink {iteration} {len(stones1)}")
    if iteration == 0:
        return stones1

    #split stones then return list of split stones
    stones1 = splitting(stones1)
    return parse_stones(stones1, iteration-1)



def splitting(stones2):
    if len(stones2) == 1:
        stone = stones2[0]
        digits = len(str(stone))
        if stone == 0:
            stones2 = [1]
        elif digits % 2 == 0:
            half = int(digits/2)
            stones2 = [int(str(stone)[0:half]), int(str(stone)[half:])]
        else:
            stones2 = [stone * 2024]
    else:
        for i in range(len(stones2)):
            stones3 = splitting([stones2.pop(0)])
            stones2 += stones3

    return stones2

        

print(len(parse_stones(inp, 40)))
