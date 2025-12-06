import sys

def print_dic(a):
    for r in range(0, maxrow):
        for c in range(0, maxcol):
            try:
                print(a[complex(r,c)], end="")
            except:
                print(" ", end="")
        print()

def grid2cplxdic(grid, ignore_chars=""):
    """
    converts traditional [x(column), y(row)] grid into a dic with inverted coordinates
    based on complex numbers:
    returns: row + col j with their value
    0+0j ----> 0+9j
      |          |
      |          |
    9+0j ----> 9+9j
    """
    dic = {}
    ignore = set(ignore_chars)
    for row, line in enumerate(grid):
        for col, char in enumerate(line):
            if char in ignore: continue
            dic[complex(row, col)] = char
    return dic
    # parsing such dic:  for k, v in dic.items()
##########

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n")

grid = grid2cplxdic(t)
summ = 0

while True:
    toremove = []
    for k, v in grid.items():
        neib = 0
        if '@' in v:
            for n in [-1, 1, -1j, 1j, -1-1j, -1+1j, 1-1j, 1+1j]:
                try:
                    if '@' in grid[k+n]:
                        neib += 1
                        if neib >3:
                            break
                except: pass
            if neib <=3:
                summ += 1
                toremove.append(k)
    for k in toremove:
        grid[k] = 'x'
    if len(toremove) < 1:
        break

print(summ)
