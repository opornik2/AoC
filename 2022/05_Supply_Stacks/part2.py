#!/usr/bin/env python3

import sys
import re
#             [L] [M]         [M]
#         [D] [R] [Z]         [C] [L]
#         [C] [S] [T] [G]     [V] [M]
# [R]     [L] [Q] [B] [B]     [D] [F]
# [H] [B] [G] [D] [Q] [Z]     [T] [J]
# [M] [J] [H] [M] [P] [S] [V] [L] [N]
# [P] [C] [N] [T] [S] [F] [R] [G] [Q]
# [Z] [P] [S] [F] [F] [T] [N] [P] [W]
#  1   2   3   4   5   6   7   8   9

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split('\n')

st = {}
st[1]=['Z','P','M','H','R']
st[2]=['P','C','J','B']
st[3]=['S','N','H','G','L','C','D']
st[4]=['F','T','M','D','Q','S','R','L']
st[5]=['F','S','P','Q','B','T','Z','M']
st[6]=['F','T','S','Z','B','G']
st[7]=['N','R','V']
st[8]=['P','G','L','T','D','V','C','M']
st[9]=['W','Q','N','J','F','M','L']

for line in t:
    print(line)
    for i in range(1,10):
        print(st[i])
    (x, no, x, fr, x, to) = line.split(' ')
    no = int(no)
    fr = int(fr)
    to = int(to)
    take = st[fr][-no:]
    print("take: "+str(take))
    del st[fr][-no:]
    st[to] += take

for i in range(1,10):
    print(st[i].pop(), end="")
