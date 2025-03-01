file = open("./input.txt", "r")
lines = file.readlines()

# Part 1
lightGrid = []

# Remplissage de la grille de lumières avec un booléen d'état allumée / éteinte
for i in range(1000):
    line = []
    for j in range(1000):
        line.append(False)
    lightGrid.append(line)

for line in lines:
    data = line.replace("turn ", "").replace("\n", "").split(" ")
    
    # Split des coordonnées des lumières
    data[1] = data[1].split(",")
    data[3] = data[3].split(",")

    xStart = int(data[1][0])
    xEnd = int(data[3][0])
    yStart = int(data[1][1])
    yEnd = int(data[3][1])

    match data[0]:
        case "on":
            for i in range(xStart, xEnd+1):
                for j in range(yStart, yEnd+1):
                    lightGrid[i][j] = True
        case "off":
            for i in range(xStart, xEnd+1):
                for j in range(yStart, yEnd+1):
                    lightGrid[i][j] = False
        case "toggle":
            for i in range(xStart, xEnd+1):
                for j in range(yStart, yEnd+1):
                    lightGrid[i][j] = not lightGrid[i][j]

print(sum(line.count(True) for line in lightGrid))

# Part 2
lightGrid = []

# Remplissage de la grille de lumières avec un booléen d'état allumée / éteinte
for i in range(1000):
    line = []
    for j in range(1000):
        line.append(0)
    lightGrid.append(line)

for line in lines:
    data = line.replace("turn ", "").replace("\n", "").split(" ")
    
    # Split des coordonnées des lumières
    data[1] = data[1].split(",")
    data[3] = data[3].split(",")

    xStart = int(data[1][0])
    xEnd = int(data[3][0])
    yStart = int(data[1][1])
    yEnd = int(data[3][1])

    match data[0]:
        case "on":
            for i in range(xStart, xEnd+1):
                for j in range(yStart, yEnd+1):
                    lightGrid[i][j] += 1
        case "off":
            for i in range(xStart, xEnd+1):
                for j in range(yStart, yEnd+1):
                    lightGrid[i][j] -= 1 if lightGrid[i][j] > 0 else lightGrid[i][j]
        case "toggle":
            for i in range(xStart, xEnd+1):
                for j in range(yStart, yEnd+1):
                    lightGrid[i][j] += 2

print(sum(sum(lightGrid, [])))