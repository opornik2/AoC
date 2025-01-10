#!/usr/bin/env python3

import sys

debug = True if "debug" in sys.argv else False
intest = False
opcode = {0: "adv", 1: "bxl", 2: "bst", 3: "jnz", 4: "bxc", 5: "outp", 6: "bdv", 7:"cdv"}
out = []

def tests():
    #unit tests
    global intest, A, B, C
    intest = True

    #opcode 0
    A = 2013
    adv(3) # 2013// 2**3
    assert A == 251
    B=4
    adv(5) # 251// 2**4
    assert A == 15

    #opcode 1
    B = 29
    bxl(7)
    assert B == 26

    B = 10
    bxl(5)
    assert B == 15

    #opcode 2
    C = 9
    bst(6)
    assert B == 1

    #opcode 4
    B = 2024
    C = 43690
    bxc(0)
    assert B == 44354

    #opcode 5
    A = 10
    B = 11
    C = 12
    assert outp(0) == 0
    assert outp(1) == 1
    assert outp(2) == 2
    assert outp(3) == 3
    assert outp(4) == 2
    assert outp(5) == 3
    assert outp(6) == 4

    #opcode 6
    A = 2013
    bdv(3) # 2013// 2**3
    assert B == 251

    #opcode 7
    A = 2013
    cdv(3) # 2013// 2**3
    assert C == 251

    intest = False

def adv(o):
    global A
    o = oper(o)
    if debug: print(f"A := {A} >> {o}")
    A = A // (2 ** o)   # 2 to the power of operand

def bxl(o):
    global B
    if debug: print(f"B := {B} xor {o}")
    B = B ^ o     # logical XOR

def bst(o):
    global B
    o = oper(o)
    if debug: print(f"B := {o} mod 8")
    B = o % 8

def jnz(o):
    global ptr
    if A == 0: ptr += 2
    else: ptr = o

def bxc(o):
    global B
    if debug: print(f"B := B mod C = {B} mod {C}")
    B = B ^ C

def outp(o):
    o = oper(o)
    #if not debug and not intest:
        #print(o % 8, end = "")
    out.append(o % 8)
    if debug: print(f"OUT {o} mod 8 = {o % 8}")
    return o % 8

def bdv(o):
    global B
    o = oper(o)
    if debug: print(f"B := A >> {o}")
    B = A // (2 ** o)   # 2 to the power of operand

def cdv(o):
    global C
    o = oper(o)
    if debug: print(f"C := A >> {o}")
    C = A // (2 ** o)   # 2 to the power of operand

def oper(o):
    if o <=3: return o
    elif o == 4: return A
    elif o == 5: return B
    elif o == 6: return C
    else: 
        print("operand error 1")


if __name__ == "__main__":
    #tests()
    out.clear()
    A = B = C = ptr = 0
    with open(sys.argv[1], mode='r') as input:
        t = input.read().strip().split("\n")

    while t:
        A = int(t.pop(0).split(": ")[1])
        B = int(t.pop(0).split(": ")[1])
        C = int(t.pop(0).split(": ")[1])
        t.pop(0)
        prog = list(map(int, t.pop(0).split(": ")[1].split(",")))
    
    for newA in range(8,8+64):
        A = newA
        ptr = 0
        B = C = 0
        stop = 0
        while True:
            try:
                opc = opcode[prog[ptr]]
                func = globals()[opc]
                operand = prog[ptr+1]
                if debug: 
                    print(f"A:{A}\tB:{B}\tC:{C}")
                    #if opc == "outp": print(f"{ptr}\t({prog[ptr]}){opc} {operand}\t output: {oper(operand) % 8}\t", end="")
                    #else:           print(f"{ptr}\t({prog[ptr]}){opc} {operand}\t", end="")
                    print(f"{ptr}\t({prog[ptr]}){opc} {operand}\t", end="")
                result = func(operand)
                if opc == "outp" and prog[15] == result:
                    print(f"Second A is {newA}")
                    stop += 1
                    break
                 
                if opc != "jnz": ptr += 2
                #if ptr == len(prog)-2: break
            except:
                break
        if stop: break

    print(out)