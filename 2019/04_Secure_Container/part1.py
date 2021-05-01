#!/bin/env python

import sys

count = 0
for l in range(264793, 803936):
	t = [int(d) for d in str(l)]
	if t[0]==t[1] or t[1]==t[2] or t[2]==t[3] or t[3]==t[4] or t[4]==t[5]:
		if t[0]<=t[1] and t[1]<=t[2] and t[2]<=t[3] and t[3]<=t[4] and t[4]<=t[5]:
			count += 1
			print(l)

print("matches: "+str(count))

