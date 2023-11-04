#!/usr/bin/env python3

import sys

with open('input', mode='r') as input:
    t = input.read().strip().split("\n")
dimen=0
ribbon=0
for line in t:
    l,w,h=map(int, line.split("x"))
    dimen += 2*(l*w + l*h + w*h) + min(l*w, l*h, w*h)
    ribbon += 2*(l + w + h - max(l, w, h)) + l*w*h
print(f"paper: {dimen}")
print(f"ribbon: {ribbon}")


