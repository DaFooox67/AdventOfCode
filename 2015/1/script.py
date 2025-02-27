file = open("./input.txt", "r")
input = file.read()

# Part 1
floor = 0

for char in input:
    match char:
        case "(":
            floor += 1
        case ")":
            floor -= 1

print(floor)

# Part 2
floor = 0
charPos = 0

for char in input:
    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1
    charPos += 1
    if (floor == -1):
        break

print(charPos)