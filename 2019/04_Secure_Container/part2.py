#!/bin/env python

import sys, re

def tests():
	t = [int(d) for d in str(l)]
	pair = 0
	for i in range(1, len(t)):
		if t[i-1] > t[i]:
			return 0
	for i in range(0, len(t)):
		digit = t[i]
		if re.search(str(digit)+"{2}", str(l)):
			if re.search(str(digit)+"{3}", str(l)):
				continue
			else:
				pair = 1
				break

	print("%i\t%i" % (l, pair))
	if pair == 1:
		return 1
	else:
		return 0


count = 0
for l in range(264793, 803936):
#for l in range(266777, 803936):
	if tests() != 0:
		count += 1
print("matches: "+str(count))

