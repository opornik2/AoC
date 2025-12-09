#!/usr/bin/env python3

import sys

debug = 1
def log(x):
    if debug:
        print(x)

with open(sys.argv[1], mode='r') as input:
    (ranges_s, avail_s) = input.read().strip().split('\n\n')

ranges_lines = ranges_s.split("\n")
ranges = []
total = 0
for r in ranges_lines:
    (start,end) = r.split("-")
    #union of previous and new set(range), out om memory!!!
    #idlist |= set(range(int(start), int(end)+1))   #union of previous and new set(range)
    #the same for this
    #concat_ranges = itertools.chain(concat_ranges, range(int(start), int(end)+1))
    ranges.append( (int(start), int(end)) )

ranges2 = []
while ranges:
    (start, end) = ranges.pop(0)
    log(f"checking {start}-{end}")
    for (s, e) in ranges:
        log(f"    against {s}-{e}")
        if start >= s and end <= e:  #range is inside other range -> remove it
            log(f"    source smaller, removing {start}-{end}")
        elif s <= start <= e <= end: #range ovelaps other range
            log(f"    source overlaps high")
            start = e + 1
            log(f"      shrinking source to {start}-{end}")
        elif start <= s <= end <= e:
            log(f"    source overlaps low")
            end = s - 1
            log(f"      shrinking source to {start}-{end}")
    ranges2.append( (start, end) )


while ranges2:
     (start, end) = ranges2.pop(0)
     total += end - start + 1

print(total)
