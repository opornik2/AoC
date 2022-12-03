#!/usr/bin/env python3

import sys
#1 Rock  A X
#2 Paper B Y
#3 Sciss C Z
#lose X 0
#draw Y 3
#win  Z 6

with open('input', mode='r') as input:
    t = input.read().strip().split('\n')

score = 0
for e in t:
    
    if e=="A X": score += 3
    elif e=="A Y": score += 4
    elif e=="A Z": score += 8
    elif e=="B X": score += 1
    elif e=="B Y": score += 5
    elif e=="B Z": score += 9
    elif e=="C X": score += 2
    elif e=="C Y": score += 6
    elif e=="C Z": score += 7

print(str(score))


