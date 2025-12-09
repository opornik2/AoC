import sys

debug = True if "debug" in sys.argv else False

def log(x):
    if debug:
        print(x)

with open(sys.argv[1], mode='r') as input:
    t = input.read().rstrip("\n").split("\n")

red = []
for l in t:
    (x, y) = l.split(",")
    red.append(complex(int(x), int(y)))

maxsize = 0
for t1 in range(len(red)-1):
    log(red[t1])
    for t2 in range(1, len(red)):
        log(f"    {red[t2]}")
        size = (1 + abs(red[t1].real - red[t2].real)) * (1 + abs(red[t1].imag - red[t2].imag))
        log(f"        {size}")
        if size > maxsize:
            maxsize = size

print(maxsize)