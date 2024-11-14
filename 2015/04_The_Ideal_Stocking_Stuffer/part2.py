#!/bin/env python3
import hashlib

key = "iwrupvqb"
salt = 0
while True:
    full = key+str(salt)
    result = hashlib.md5(full.encode())
    start = result.hexdigest()[0:6]
    if start == "000000":
        print(salt)
        break
    salt += 1

