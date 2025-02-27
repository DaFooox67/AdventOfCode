import numpy as np

file = open("./input.txt", "r")
input = file.read()

# Part 1
position = [0, 0]
gifted = [[0, 0]]

for char in input:
    match char:
        case "^":
            position[1] += 1
        case "v":
            position[1] -= 1
        case ">":
            position[0] += 1
        case "<":
            position[0] -= 1
    
    # Si la maison n'a pas encore été livrée, on l'ajoute à cette liste
    if (position not in gifted):
        gifted.append(position.copy())

print(len(gifted))

# Part 2
santaPosition = [0, 0]
roboSantaPosition = [0, 0]
gifted = [[0, 0]]
charPos = 1

for char in input:
    match charPos % 2:
        case 0:
            match char:
                case "^":
                    santaPosition[1] += 1
                case "v":
                    santaPosition[1] -= 1
                case ">":
                    santaPosition[0] += 1
                case "<":
                    santaPosition[0] -= 1
        case 1:
            match char:
                case "^":
                    roboSantaPosition[1] += 1
                case "v":
                    roboSantaPosition[1] -= 1
                case ">":
                    roboSantaPosition[0] += 1
                case "<":
                    roboSantaPosition[0] -= 1

    # Si la maison n'a pas encore été livrée, on l'ajoute à cette liste
    if (santaPosition not in gifted):
        gifted.append(santaPosition.copy())
    if (roboSantaPosition not in gifted):
        gifted.append(roboSantaPosition.copy())
    
    charPos += 1

print(len(gifted))