#!/usr/bin/env python3

import sys
import re

debug = 0

def log(x):
    if debug:
        print(x)

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split(",")

summ=0
for line in t:
    (start, end) = line.split("-")
    # naive bruteforce for all numbers in all ranges
    for el in range(int(start),int(end)+1):
        cnt = 1
        while cnt <= len(str(el))//2:
            pat = re.compile(r'\d{'+str(cnt)+'}')
            #convert list of found patterns to a set which removes duplicates
            #if length of such set is 1 then all patterns are the same
            if len(set(re.findall(pat, str(el)))) == 1 and cnt * len(re.findall(pat, str(el))) == len(str(el)):
                summ += el
                log(el)
                cnt += 100
            cnt += 1

print(summ)
