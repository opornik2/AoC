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

for (start, end) in ranges:
    log(f"checking {start}-{end}")
    for (s, e) in ranges:
        log(f"against {s}-{e}")
        if start == s and end == e:
            continue
        if start >= s and end <= e:  #range is smaller than other range -> remove it
            log(f"source smaller, removing {start}-{end}")
            ranges.remove( (start, end) )
        elif s <= start <= e and end >= e: #range ovelaps other range
            total += end - s + 1
            log(f"source overlaps high, removing both")
            ranges.remove( (start, end) )
            ranges.remove( (s, e) )
        elif start <= s <= end and end <= e:
            total += e - start + 1
            log(f"source overlaps low, removing both")
            ranges.remove( (start, end) )
            ranges.remove( (s, e) )
    total += end - start + 1
    log(f"total={total}")
    #ranges.remove( (start, end) )

print(total)
