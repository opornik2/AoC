#!/bin/env python

import sys
d = {}
counter = 0

def count(k):
	global counter
	try:
		loc_v = d[k]
		count(loc_v)
		counter += 1
	except:
		return

with open('input', mode='r') as input:
	t = input.read().split()

for el in t:
	v = el.split(')')[0]
	k = el.split(')')[1]
	d[k] = v

for el in d.keys():
	counter += 1
	count(d[el])

print(counter)

