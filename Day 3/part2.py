import sys

# we need to check 8 directions for each digit
# any digit in a number adjacent to a symbol is a part number
# numbers can have 1 to N digits 
#def isAdjacentToSymbol:

# hopefully there are no letters, and letters aren't considered symbols
# we'll assume a symbol is any special character, except a period
def isSymbol(char):
    if(char == '.' or char.isalpha() or char.isdigit()):
        return False
    return True

# we assume numbers don't cross over to new lines
def isFirstDigit(char, line, index):
    if(index == 0 and char.isdigit()):
        return True
    if(not char.isdigit() or line[index-1].isdigit()):
        return False
    return True

def isLastDigit(char, line, index):
    if(index == len(line)-1 and char.isdigit()):
        return True
    if(not char.isdigit() or line[index+1].isdigit()):
        return False
    return True

# we can take this a step further
# we need a simple way of defining which directions to check
# a character needs to be checked 3, 5 or 8 directions
# a corner character needs to be checked 3 directions
# a border character that is not a corner needs to be checked 5 directions
# a non-border character needs to be checked 8 directions
# def isBorderChar(char, charIndex, line, lineIndex, content):
#     if(charIndex == 0 or charIndex == len(line)-1):
#         return True
#     if(lineIndex == 0 or lineIndex == len(content)-1):
#         return True
#     return False

def getBorderType(char, charIndex, line, lineIndex, content):
    if(charIndex == len(line)-1 and lineIndex == 0):
        return "northEast"
    if(charIndex == len(line)-1 and lineIndex == len(content)-1):
        return "southEast"
    if(charIndex == 0 and lineIndex == len(content)-1):
        return "southWest"
    if(charIndex == 0 and lineIndex == 0):
        return "northWest"
    if(lineIndex == 0):
        return "north"
    if(charIndex == len(line)-1):
        return "east"
    if(lineIndex == len(content)-1):
        return "south"
    if(charIndex == 0):
        return "west"
    return "central"

def northEastAdjacent(char, charIndex, line, lineIndex, content):
    if(isSymbol(line[charIndex-1])):
        return True
    if(isSymbol(content[lineIndex+1][charIndex-1])):
        return True
    if(isSymbol(content[lineIndex+1][charIndex])):
        return True
    return False

def southEastAdjacent(char, charIndex, line, lineIndex, content):
    if(isSymbol(line[charIndex-1])):
        return True
    if(isSymbol(content[lineIndex-1][charIndex-1])):
        return True
    if(isSymbol(content[lineIndex-1][charIndex])):
        return True
    return False

def southWestAdjacent(char, charIndex, line, lineIndex, content):
    if(isSymbol(line[charIndex+1])):
        return True
    if(isSymbol(content[lineIndex-1][charIndex+1])):
        return True
    if(isSymbol(content[lineIndex-1][charIndex])):
        return True
    return False

def northWestAdjacent(char, charIndex, line, lineIndex, content):
    if(isSymbol(line[charIndex+1])):
        return True
    if(isSymbol(content[lineIndex+1][charIndex+1])):
        return True
    if(isSymbol(content[lineIndex+1][charIndex])):
        return True
    return False

def northAdjacent(char, charIndex, line, lineIndex, content):
    if(isSymbol(line[charIndex-1])):
        return True
    if(isSymbol(line[charIndex+1])):
        return True
    if(isSymbol(content[lineIndex+1][charIndex-1])):
        return True
    if(isSymbol(content[lineIndex+1][charIndex])):
        return True
    if(isSymbol(content[lineIndex+1][charIndex+1])):
        return True
    return False

def eastAdjacent(char, charIndex, line, lineIndex, content):
    if(isSymbol(line[charIndex-1])):
        return True
    if(isSymbol(content[lineIndex-1][charIndex-1])):
        return True
    if(isSymbol(content[lineIndex-1][charIndex])):
        return True
    if(isSymbol(content[lineIndex+1][charIndex-1])):
        return True
    if(isSymbol(content[lineIndex+1][charIndex])):
        return True
    return False

def southAdjacent(char, charIndex, line, lineIndex, content):
    if(isSymbol(line[charIndex-1])):
        return True
    if(isSymbol(line[charIndex+1])):
        return True
    if(isSymbol(content[lineIndex-1][charIndex-1])):
        return True
    if(isSymbol(content[lineIndex-1][charIndex])):
        return True
    if(isSymbol(content[lineIndex-1][charIndex+1])):
        return True
    return False

def westAdjacent(char, charIndex, line, lineIndex, content):
    if(isSymbol(line[charIndex+1])):
        return True
    if(isSymbol(content[lineIndex-1][charIndex])):
        return True
    if(isSymbol(content[lineIndex-1][charIndex+1])):
        return True
    if(isSymbol(content[lineIndex+1][charIndex])):
        return True
    if(isSymbol(content[lineIndex+1][charIndex+1])):
        return True
    return False

def centralAdjacent(char, charIndex, line, lineIndex, content):
    if(isSymbol(line[charIndex-1])):
        return True
    if(isSymbol(line[charIndex+1])):
        return True
    if(isSymbol(content[lineIndex-1][charIndex-1])):
        return True
    if(isSymbol(content[lineIndex-1][charIndex])):
        return True
    if(isSymbol(content[lineIndex-1][charIndex+1])):
        return True
    if(isSymbol(content[lineIndex+1][charIndex-1])):
        return True
    if(isSymbol(content[lineIndex+1][charIndex])):
        return True
    if(isSymbol(content[lineIndex+1][charIndex+1])):
        return True
    return False

def isAdjacent(borderType, char, charIndex, line, lineIndex, content):
    if(borderType == "northEast"):
        return northEastAdjacent(char, charIndex, line, lineIndex, content)
    if(borderType == "southEast"):
        return southEastAdjacent(char, charIndex, line, lineIndex, content)
    if(borderType == "southWest"):
        return southWestAdjacent(char, charIndex, line, lineIndex, content)
    if(borderType == "northWest"):
        return northWestAdjacent(char, charIndex, line, lineIndex, content)
    if(borderType == "north"):
        return northAdjacent(char, charIndex, line, lineIndex, content)
    if(borderType == "east"):
        return eastAdjacent(char, charIndex, line, lineIndex, content)
    if(borderType == "south"):
        return southAdjacent(char, charIndex, line, lineIndex, content)
    if(borderType == "west"):
        return westAdjacent(char, charIndex, line, lineIndex, content)
    if(borderType == "central"):
        return centralAdjacent(char, charIndex, line, lineIndex, content)
    return False

def getNorthEastAdjacentNumbers(char, charIndex, line, lineIndex, content):
    adjacentNumbers = []

    westChar = line[charIndex-1]
    if(westChar.isdigit()):
        adjacentNumbers.append(getNumber(westChar, charIndex-1, line))

    southWestChar = content[lineIndex+1][charIndex-1]
    southChar = content[lineIndex+1][charIndex]
    if(southWestChar.isdigit()):
        adjacentNumbers.append(getNumber(southWestChar, charIndex-1, content[lineIndex+1]))
    elif(southChar.isdigit()):
        adjacentNumbers.append(getNumber(southChar, charIndex, content[lineIndex+1]))

    return adjacentNumbers

def getSouthEastAdjacentNumbers(char, charIndex, line, lineIndex, content):
    adjacentNumbers = []

    westChar = line[charIndex-1]
    if(westChar.isdigit()):
        adjacentNumbers.append(getNumber(westChar, charIndex-1, line))

    northWestChar = content[lineIndex-1][charIndex-1]
    northChar = content[lineIndex-1][charIndex]
    if(northWestChar.isdigit()):
        adjacentNumbers.append(getNumber(northWestChar, charIndex-1, content[lineIndex-1]))
    elif(northChar.isdigit()):
        adjacentNumbers.append(getNumber(northChar, charIndex, content[lineIndex-1]))

    return adjacentNumbers

def getSouthWestAdjacentNumbers(char, charIndex, line, lineIndex, content):
    adjacentNumbers = []
    
    eastChar = line[charIndex+1]
    if(eastChar.isdigit()):
        adjacentNumbers.append(getNumber(eastChar, charIndex+1, line))
    
    northEastChar = content[lineIndex-1][charIndex+1]
    northChar = content[lineIndex-1][charIndex]
    if(northEastChar.isdigit()):
        adjacentNumbers.append(getNumber(northEastChar, charIndex+1, content[lineIndex-1]))
    elif(northChar.isdigit()):
        adjacentNumbers.append(getNumber(northChar, charIndex, content[lineIndex-1]))

    return adjacentNumbers

def getNorthWestAdjacentNumbers(char, charIndex, line, lineIndex, content):
    adjacentNumbers = []

    eastChar = line[charIndex+1]
    if(eastChar.isdigit()):
        adjacentNumbers.append(getNumber(eastChar, charIndex+1, line))

    southEastChar = content[lineIndex+1][charIndex+1]
    southChar = content[lineIndex+1][charIndex]
    if(southEastChar.isdigit()):
        adjacentNumbers.append(getNumber(southEastChar, charIndex+1, content[lineIndex+1]))
    elif(southChar.isdigit()):
        adjacentNumbers.append(getNumber(southChar, charIndex, content[lineIndex+1]))
    
    return adjacentNumbers

def getNorthAdjacentNumbers(char, charIndex, line, lineIndex, content):
    adjacentNumbers = []

    westChar = line[charIndex-1]
    if(westChar.isdigit()):
        adjacentNumbers.append(getNumber(westChar, charIndex-1, line))
    
    eastChar = line[charIndex+1]
    if(eastChar.isdigit()):
        adjacentNumbers.append(getNumber(eastChar, charIndex+1, line))
    
    southChar = content[lineIndex+1][charIndex]
    if(southChar.isdigit()):
        adjacentNumbers.append(getNumber(southChar, charIndex, content[lineIndex+1]))
    else:
        southWestChar = content[lineIndex+1][charIndex-1]
        southEastChar = content[lineIndex+1][charIndex+1]
        if(southWestChar.isdigit()):
            adjacentNumbers.append(getNumber(southWestChar, charIndex-1, content[lineIndex+1]))
        if(southEastChar.isdigit()):
            adjacentNumbers.append(getNumber(southEastChar, charIndex+1, content[lineIndex+1]))

    return adjacentNumbers

def getEastAdjacentNumbers(char, charIndex, line, lineIndex, content):
    adjacentNumbers = []

    northWestChar = content[lineIndex-1][charIndex-1]
    northChar = content[lineIndex-1][charIndex]
    if(northWestChar.isdigit()):
        adjacentNumbers.append(getNumber(northWestChar, charIndex-1, content[lineIndex-1]))
    elif(northChar.isdigit()):
        adjacentNumbers.append(getNumber(northChar, charIndex, content[lineIndex-1]))
    
    southWestChar = content[lineIndex+1][charIndex-1]
    southChar = content[lineIndex+1][charIndex]
    if(southWestChar.isdigit()):
        adjacentNumbers.append(getNumber(southWestChar, charIndex-1, content[lineIndex+1]))
    elif(southChar.isdigit()):
        adjacentNumbers.append(getNumber(southChar, charIndex, content[lineIndex+1]))
    
    westChar = line[charIndex-1]
    if(westChar.isdigit()):
        adjacentNumbers.append(getNumber(westChar, charIndex-1, line))
    
    return adjacentNumbers

def getSouthAdjacentNumbers(char, charIndex, line, lineIndex, content):
    adjacentNumbers = []

    westChar = line[charIndex-1]
    if(westChar.isdigit()):
        adjacentNumbers.append(getNumber(westChar, charIndex-1, line))
    
    eastChar = line[charIndex+1]
    if(eastChar.isdigit()):
        adjacentNumbers.append(getNumber(eastChar, charIndex+1, line))
    
    northChar = content[lineIndex-1][charIndex]
    if(northChar.isdigit()):
        adjacentNumbers.append(getNumber(northChar, charIndex, content[lineIndex-1]))
    else:
        northWestChar = content[lineIndex-1][charIndex-1]
        northEastChar = content[lineIndex-1][charIndex+1]
        if(northWestChar.isdigit()):
            adjacentNumbers.append(getNumber(northWestChar, charIndex-1, content[lineIndex-1]))
        if(northEastChar.isdigit()):
            adjacentNumbers.append(getNumber(northEastChar, charIndex+1, content[lineIndex-1]))

    return adjacentNumbers

# should these define the location of each number?????????
def getWestAdjacentNumbers(char, charIndex, line, lineIndex, content):
    adjacentNumbers = []

    northEastChar = content[lineIndex-1][charIndex+1]
    northChar = content[lineIndex-1][charIndex]
    if(northEastChar.isdigit()):
        adjacentNumbers.append(getNumber(northEastChar, charIndex+1, content[lineIndex-1]))
    elif(northChar.isdigit()):
        adjacentNumbers.append(getNumber(northChar, charIndex, content[lineIndex-1]))
    
    southEastChar = content[lineIndex+1][charIndex+1]
    southChar = content[lineIndex+1][charIndex]
    if(southEastChar.isdigit()):
        adjacentNumbers.append(getNumber(southEastChar, charIndex+1, content[lineIndex+1]))
    elif(southChar.isdigit()):
        adjacentNumbers.append(getNumber(southChar, charIndex, content[lineIndex+1]))
    
    eastChar = line[charIndex+1]
    if(eastChar.isdigit()):
        adjacentNumbers.append(getNumber(eastChar, charIndex+1, line))
    
    return adjacentNumbers

def getCentralAdjacentNumbers(char, charIndex, line, lineIndex, content):
    adjacentNumbers = []

    # check north
    northChar = content[lineIndex-1][charIndex]
    if(northChar.isdigit()):
        adjacentNumbers.append(getNumber(northChar, charIndex, content[lineIndex-1]))
    else:
        northWestChar = content[lineIndex-1][charIndex-1]
        northEastChar = content[lineIndex-1][charIndex+1]
        if(northWestChar.isdigit()):
            adjacentNumbers.append(getNumber(northWestChar, charIndex-1, content[lineIndex-1]))
        if(northEastChar.isdigit()):
            adjacentNumbers.append(getNumber(northEastChar, charIndex+1, content[lineIndex-1]))
    
    # check east
    eastChar = line[charIndex+1]
    if(eastChar.isdigit()):
        adjacentNumbers.append(getNumber(eastChar, charIndex+1, line))

    # check south
    southChar = content[lineIndex+1][charIndex]
    if(southChar.isdigit()):
        adjacentNumbers.append(getNumber(southChar, charIndex, content[lineIndex+1]))
    else:
        southWestChar = content[lineIndex+1][charIndex-1]
        southEastChar = content[lineIndex+1][charIndex+1]
        if(southWestChar.isdigit()):
            adjacentNumbers.append(getNumber(southWestChar, charIndex-1, content[lineIndex+1]))
        if(southEastChar.isdigit()):
            adjacentNumbers.append(getNumber(southEastChar, charIndex+1, content[lineIndex+1]))

    # check west
    westChar = line[charIndex-1]
    if(westChar.isdigit()):
        adjacentNumbers.append(getNumber(westChar, charIndex-1, line))
    
    return adjacentNumbers

def getAdjacentNumbers(char, charIndex, line, lineIndex, content):
    borderType = getBorderType(char, charIndex, line, lineIndex, content)
    if(borderType == "northEast"):
        return getNorthEastAdjacentNumbers(char, charIndex, line, lineIndex, content)
    if(borderType == "southEast"):
        return getSouthEastAdjacentNumbers(char, charIndex, line, lineIndex, content)
    if(borderType == "southWest"):
        return getSouthWestAdjacentNumbers(char, charIndex, line, lineIndex, content)
    if(borderType == "northWest"):
        return getNorthWestAdjacentNumbers(char, charIndex, line, lineIndex, content)
    if(borderType == "north"):
        return getNorthAdjacentNumbers(char, charIndex, line, lineIndex, content)
    if(borderType == "east"):
        return getEastAdjacentNumbers(char, charIndex, line, lineIndex, content)
    if(borderType == "south"):
        return getSouthAdjacentNumbers(char, charIndex, line, lineIndex, content)
    if(borderType == "west"):
        return getWestAdjacentNumbers(char, charIndex, line, lineIndex, content)
    # will always default to central
    return getCentralAdjacentNumbers(char, charIndex, line, lineIndex, content)

def isGear(char, charIndex, line, lineIndex, content):
    adjacentNumbers = getAdjacentNumbers(char, charIndex, line, lineIndex, content)
    if(char == "*" and len(adjacentNumbers) == 2):
        return True
    return False

def getFirstDigitIndex(char, charIndex, line):
    index = charIndex
    while index >= 0:
        if not line[index].isdigit():
            return index+1
        index -= 1
    return 0

def getLastDigitIndex(char, charIndex, line):
    index = charIndex
    while index < len(line):
        if not line[index].isdigit():
            return index-1
        index += 1
    return len(line)-1

def getNumber(char, charIndex, line):
    if(char.isdigit()):
        firstDigitIndex = getFirstDigitIndex(char, charIndex, line)
        lastDigitIndex = getLastDigitIndex(char, charIndex, line)
        return line[firstDigitIndex:lastDigitIndex+1]
    return False

if(sys.argv[1]):
    filename = sys.argv[1]
else:
    print("No filename provided")
    exit()

with open(filename) as f:
    content = f.readlines()
    sum = 0
    
    # line iterator
    lineIndex = 0
    while lineIndex < len(content):
        if lineIndex != 0:
            previousLine = content[lineIndex-1].strip()

        currentLine = content[lineIndex].strip()

        if lineIndex != len(content)-1:
            nextLine = content[lineIndex+1].strip()

        numberHasAdjacent = False
        # character iterator. we're assuming every line has the same length
        charIndex = 0
        while charIndex < len(currentLine):
            currentChar = currentLine[charIndex]
            if(currentChar == "*"):
                adjacentNumbers = getAdjacentNumbers(currentChar, charIndex, currentLine, lineIndex, content)
                if(len(adjacentNumbers) == 2):
                    # multiply the values
                    gearRatio = int(adjacentNumbers[0]) * int(adjacentNumbers[1])
                    sum += gearRatio
                    print(currentChar, adjacentNumbers, gearRatio, sum)

            charIndex += 1
        lineIndex += 1