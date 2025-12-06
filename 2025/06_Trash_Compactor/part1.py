#!/usr/bin/env python3

import sys
import re

def array_transform(X):
    return [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

with open(sys.argv[1], mode='r') as input:
    lines = input.read().strip().split('\n')

total = 0
matrix = []
for l in lines:
    l = re.sub(" +", " ", l)
    matrix.append(l.strip().split(" "))

matrixt = array_transform(matrix)
for task in matrixt:
    op = task.pop()
    if '+' in op:
        summ = 0
        for num in task:
            summ += int(num)
    elif '*' in op:
        summ = 1
        for num in task:
            summ *= int(num)
    else:
         print ("Error with operand")
    total += summ

print(total)

