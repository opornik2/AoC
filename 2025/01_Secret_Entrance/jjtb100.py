with open("input") as f:
    lines = f.readlines()

input = list(line.strip() for line in lines)

number = 50
ans  = 0
for line in input:
    prev = number
    if line[0] == "L":
        number -= int(line[1:])
        ans += (prev - 1) // 100 - (number - 1) // 100
    elif line[0] == "R":
        number += int(line[1:])
        ans += number // 100 - prev // 100
        



print(ans)
