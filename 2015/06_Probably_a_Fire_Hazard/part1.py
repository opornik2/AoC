#!/usr/bin/env python3

import sys
import re

cnt = 0

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n")

for line in t:
    print(line)


