#!/usr/bin/env python3
import sys
import time
from heapq import heapify, heappop, heappush

debug = True if "debug" in sys.argv else False

with open(sys.argv[1], mode='r') as inp:
    t = inp.read().strip().split("\n")


