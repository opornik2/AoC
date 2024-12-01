#!/bin/env python3
import hashlib

passstring = "cqjxjnds"
passstring = "cqjxxyzz"
password = list(passstring)

def nextpass(position):
    code = ord(password[position]) - 97
    code = (code + 1) % 26
    if code == 0:
        nextpass(position - 1)
    password[position] = chr(code + 97)
    return
    
def checkpass():
    passed1 = passed2 = 0
    if "i" in password or "o" in password or "l" in password:
        return False
    double = ""
    for i in range(7):
        if i<6 and ord(password[i])+1 == ord(password[i+1]) and ord(password[i])+2 == ord(password[i+2]):
            passed1 += 1
        if password[i] == password[i+1]:
            if not double:
                double = password[i]
            else:
                if password[i] == password[i+1] and double != password[i]:
                    passed2 += 1
                    #print(password[i])

    if passed1 and passed2:
        print("".join(password))
        print("passed all tests")
        return True
    else:
        return False
    
    

while True:
    nextpass(7)
    if checkpass():
        break

