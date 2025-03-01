file = open("./input.txt", "r")
lines = file.readlines()

vowels = ["a", "e", "i", "o", "u"]
forbiddenStrings = ["ab", "cd", "pq", "xy"]

# Part 1
niceStrings = 0

for line in lines:
    vowelsCount = 0
    doubleLetter = False
    forbiddenString = False
    previousChar = ""

    for char in line:
        if char in vowels:
            vowelsCount += 1
        if char == previousChar:
            doubleLetter = True
        if previousChar + char in forbiddenStrings:
            forbiddenString = True
        
        previousChar = char

    if vowelsCount >= 3 and doubleLetter and forbiddenString == False:
        niceStrings += 1

print(niceStrings)

# Part 2
niceStrings = 0

for line in lines:
    charList = []
    stringPairs = []
    pairOfTwoLetters = False
    repeatedLetter = False

    for char in line.replace("\n", ""):
        charList.append(char)
    
    for i in range(1, len(charList)):
        stringPair = charList[i-1] + charList[i]
        stringPairs.append(stringPair)

        if stringPairs.count(stringPair) == 2 and stringPairs.index(stringPair) != i-2:
            pairOfTwoLetters = True

        if i < len(charList) - 1:
            if charList[i+1] == charList[i-1]:
                repeatedLetter = True

    if pairOfTwoLetters and repeatedLetter:
        niceStrings += 1

print(niceStrings)