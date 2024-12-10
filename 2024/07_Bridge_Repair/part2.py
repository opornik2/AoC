#!/usr/bin/env python3

import sys
import itertools

debug = True

def find_operators(res):
    operators = len(nums) - 1
    for op in itertools.product("+|*", repeat=operators):
        eq = str(nums[0])
        for i in range(operators):
            if "|" in op[i]: oper = ""
            else: oper = op[i]
            eqs = str(eq) + str(oper) + str(nums[i+1])
            eq = eval(eqs)
            if eq > res: break  # no sense to check rest of operators is partial result > result
        if eq == res:
            if debug: print(f"{res} = {eqs}")
            return True
    return False

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n")

summ = 0
for line in t:
    (res, numbers) = line.split(": ")
    nums = list(map(int, numbers.split(" ")))
    res = int(res)
    if find_operators(res):
        summ += res

print(summ)