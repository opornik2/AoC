#!/usr/bin/env python3
import sys

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n")

safe = 0
for line in t:
    rap = line.split(" ")
    rap = [int(el) for el in rap]
    incr = decr = 0
    print(rap)
    for i in range(len(rap)-1):
      if rap[i] < rap[i+1] and rap[i+1]-rap[i]<=3:
        incr += 1
      else:
        break
    for i in range(len(rap)-1):
      if rap[i] > rap[i+1] and rap[i]-rap[i+1]<=3:
        decr += 1
      else:
        break
    if abs(incr-decr) == len(rap)-1:
      safe += 1
      print("safe")
      
print(safe)