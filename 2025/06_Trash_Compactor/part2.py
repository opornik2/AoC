#!/usr/bin/env python3

import sys
import re

def array_transform(X):
    return [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

with open(sys.argv[1], mode='r') as input:
    lines = input.read().split('\n')

total = 0
matrix = []
for l in lines:
    if list(l):
        matrix.append(list(l))

matrix2 = array_transform(matrix)
nums = []
for l in matrix2:
    if len(set(l)) == 1:
        if '+' in op:
            summ = 0
            for n in nums:
                summ += n
        elif '*' in op:
            summ = 1
            for n in nums:
                summ *= n
        print(f"{op} {nums} = {summ}")
        total += summ
        nums = []
        continue
    try:
        number = int("".join(l))
    except:
        op = l.pop()
        number = int("".join(l))
    nums.append(number)

if '+' in op:
    summ = 0
    for n in nums:
        summ += n
elif '*' in op:
    summ = 1
    for n in nums:
        summ *= n
print(f"{op} {nums} = {summ}")
total += summ
nums = []

print(total)

