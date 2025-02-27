import numpy as np

file = open("./input.txt", "r")
lines = file.readlines()

# Part 1
totalPaper = 0

for line in lines:
    dimensions = np.array(line.replace("\n", "").split("x")).astype(int)
    length = dimensions[0]
    width = dimensions[1]
    height = dimensions[2]

    surface = 2*length*width + 2*width*height + 2*height*length
    
    # Tri des valeurs pour obtenir le plus petit côté
    sortedDimensions = np.sort(dimensions)
    slack = int(sortedDimensions[0]) * int(sortedDimensions[1])

    totalPaper += surface + slack

print(totalPaper)

# Part 2
totalRibbon = 0

for line in lines:
    dimensions = np.array(line.replace("\n", "").split("x")).astype(int)
    length = dimensions[0]
    width = dimensions[1]
    height = dimensions[2]

    sortedDimensions = np.sort(dimensions)
    ribbonToWrap = sortedDimensions[0] + sortedDimensions[0] + sortedDimensions[1] + sortedDimensions[1]
    ribbonForBow = length * width * height

    totalRibbon += ribbonToWrap + ribbonForBow

print(totalRibbon)