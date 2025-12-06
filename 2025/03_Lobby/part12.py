import sys

#sys.argv[1]
with open(sys.argv[1], "r") as FH:
    inp = FH.read().split()

# part 1

summ = 0
for line in inp:
    hl = 0
    hr = 0
    for i in range(len(line)-1):
        digit = int(line[i])
        if digit > hr:
            hr = digit
            ridx = i
    for i in range(ridx+1, len(line)):
        digit = int(line[i])
        if digit > hl:
            hl = digit
            lidx = i
    joltage = int(str(hr) + str(hl))
    print(joltage)
    summ += joltage
    
print(summ)

# part2

summ = 0
for line in inp:
    hlist = []
    dignum = 12
    idx = 0
    for n in range(dignum):  # 0-12 cyfr
        h = 0
        for i in range(idx, len(line)-(12-n)+1):  #zaczynamy od ostatnio znalezionej w prawo
            digit = int(line[i])
            if digit > h:
                h = digit
                idx = i+1
        hlist.append(h)
        
    joltage = int("".join(map(str,hlist)))
    print(joltage)
    summ += joltage
    
print(summ)
