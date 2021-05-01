#!/usr/bin/python3

import sys
import re

debug = False
counter = 0

with open(sys.argv[1], mode='r') as inputfile:
    t = inputfile.read().split('\n\n')

for line in t:
    p = {}
    line = re.sub(r'\n', ' ', line)
    line = line.strip()
    for element in line.split(' '):
        (field, val) = element.split(':')
        p[field] = val
        if field == 'hgt' and 'cm' in val:
            p['hgtc'] = re.sub(r'cm', '', val)
            p['hgti'] = 0 
        if field == 'hgt' and 'in' in val:
            p['hgti'] = re.sub(r'in', '', val)
            p['hgtc'] = 0
    try:
        if (int(p['byr']) >= 1920 and int(p['byr']) <= 2002) \
            and (int(p['iyr']) >=2010 and int(p['iyr']) <= 2020) \
            and (int(p['eyr']) >=2020 and int(p['eyr']) <= 2030):
            if ( int(p['hgtc']) >= 150 and int(p['hgtc']) <= 193 ) or \
                ( (int(p['hgti']) >= 59 and int(p['hgti']) <= 76) ):
                if re.match(r'^#\w{6}$', p['hcl']):
                    if p['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
                        if re.match(r'^\d{9}$', p['pid']):
                            counter += 1
    except:
        pass

print(counter)

