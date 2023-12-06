#!/usr/bin/env python3

import sys
import re

time = 40817772
dist = 219101213651089

longer = 0
for k in range (1, int(time/2)+1):
    if k*(time-k) > dist:
        if k==(time-k): longer += 1
        else: longer += 2
        #print(f"{k}*{time-k}={k*(time-k)}")

print(longer)

