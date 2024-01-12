def checkStringForMapWord(inputString, map, checkKeys=True):
    if not checkKeys:
        map = map.values()

    i = 1
    while i <= len(inputString):
        j = 0
        k = i
        while k <= len(inputString):
            testSub = inputString[j:k]

            if testSub in map:
                return map[testSub]

            j += 1
            k += 1

        i += 1

    return False

# we assume a symbol is any special character, except a period


def isSymbol(char):
    if (char == '.' or char.isalpha() or char.isdigit()):
        return False
    return True

# we assume numbers don't cross over to new lines


def isFirstDigit(char, line, index):
    if (index == 0 and char.isdigit()):
        return True
    if (not char.isdigit() or line[index-1].isdigit()):
        return False
    return True


def isLastDigit(char, line, index):
    if (index == len(line)-1 and char.isdigit()):
        return True
    if (not char.isdigit() or line[index+1].isdigit()):
        return False
    return True


def getFirstDigitIndex(charIndex, line):
    index = charIndex
    while index >= 0:
        if not line[index].isdigit():
            return index+1
        index -= 1
    return 0


def getLastDigitIndex(charIndex, line):
    index = charIndex
    while index < len(line):
        if not line[index].isdigit():
            return index-1
        index += 1
    return len(line)-1


def getNumber(char, charIndex, line):
    if (char.isdigit()):
        firstDigitIndex = getFirstDigitIndex(charIndex, line)
        lastDigitIndex = getLastDigitIndex(charIndex, line)
        return line[firstDigitIndex:lastDigitIndex+1]
    return False

# a character needs to be checked 3, 5 or 8 directions
# a corner character needs to be checked 3 directions
# a border character that is not a corner needs to be checked 5 directions
# a non-border character needs to be checked 8 directions


def getBorderType(charIndex, line, lineIndex, content):
    if (charIndex == len(line)-1 and lineIndex == 0):
        return "northEast"
    if (charIndex == len(line)-1 and lineIndex == len(content)-1):
        return "southEast"
    if (charIndex == 0 and lineIndex == len(content)-1):
        return "southWest"
    if (charIndex == 0 and lineIndex == 0):
        return "northWest"
    if (lineIndex == 0):
        return "north"
    if (charIndex == len(line)-1):
        return "east"
    if (lineIndex == len(content)-1):
        return "south"
    if (charIndex == 0):
        return "west"
    return "central"


def northEastAdjacent(charIndex, line, lineIndex, content):
    if (isSymbol(line[charIndex-1])):
        return True
    if (isSymbol(content[lineIndex+1][charIndex-1])):
        return True
    if (isSymbol(content[lineIndex+1][charIndex])):
        return True
    return False


def southEastAdjacent(charIndex, line, lineIndex, content):
    if (isSymbol(line[charIndex-1])):
        return True
    if (isSymbol(content[lineIndex-1][charIndex-1])):
        return True
    if (isSymbol(content[lineIndex-1][charIndex])):
        return True
    return False


def southWestAdjacent(charIndex, line, lineIndex, content):
    if (isSymbol(line[charIndex+1])):
        return True
    if (isSymbol(content[lineIndex-1][charIndex+1])):
        return True
    if (isSymbol(content[lineIndex-1][charIndex])):
        return True
    return False


def northWestAdjacent(charIndex, line, lineIndex, content):
    if (isSymbol(line[charIndex+1])):
        return True
    if (isSymbol(content[lineIndex+1][charIndex+1])):
        return True
    if (isSymbol(content[lineIndex+1][charIndex])):
        return True
    return False


def northAdjacent(charIndex, line, lineIndex, content):
    if (isSymbol(line[charIndex-1])):
        return True
    if (isSymbol(line[charIndex+1])):
        return True
    if (isSymbol(content[lineIndex+1][charIndex-1])):
        return True
    if (isSymbol(content[lineIndex+1][charIndex])):
        return True
    if (isSymbol(content[lineIndex+1][charIndex+1])):
        return True
    return False


def eastAdjacent(charIndex, line, lineIndex, content):
    if (isSymbol(line[charIndex-1])):
        return True
    if (isSymbol(content[lineIndex-1][charIndex-1])):
        return True
    if (isSymbol(content[lineIndex-1][charIndex])):
        return True
    if (isSymbol(content[lineIndex+1][charIndex-1])):
        return True
    if (isSymbol(content[lineIndex+1][charIndex])):
        return True
    return False


def southAdjacent(charIndex, line, lineIndex, content):
    if (isSymbol(line[charIndex-1])):
        return True
    if (isSymbol(line[charIndex+1])):
        return True
    if (isSymbol(content[lineIndex-1][charIndex-1])):
        return True
    if (isSymbol(content[lineIndex-1][charIndex])):
        return True
    if (isSymbol(content[lineIndex-1][charIndex+1])):
        return True
    return False


def westAdjacent(charIndex, line, lineIndex, content):
    if (isSymbol(line[charIndex+1])):
        return True
    if (isSymbol(content[lineIndex-1][charIndex])):
        return True
    if (isSymbol(content[lineIndex-1][charIndex+1])):
        return True
    if (isSymbol(content[lineIndex+1][charIndex])):
        return True
    if (isSymbol(content[lineIndex+1][charIndex+1])):
        return True
    return False


def centralAdjacent(charIndex, line, lineIndex, content):
    if (isSymbol(line[charIndex-1])):
        return True
    if (isSymbol(line[charIndex+1])):
        return True
    if (isSymbol(content[lineIndex-1][charIndex-1])):
        return True
    if (isSymbol(content[lineIndex-1][charIndex])):
        return True
    if (isSymbol(content[lineIndex-1][charIndex+1])):
        return True
    if (isSymbol(content[lineIndex+1][charIndex-1])):
        return True
    if (isSymbol(content[lineIndex+1][charIndex])):
        return True
    if (isSymbol(content[lineIndex+1][charIndex+1])):
        return True
    return False


def isAdjacent(charIndex, line, lineIndex, content):
    borderType = getBorderType(charIndex, line, lineIndex, content)

    if (borderType == "northEast"):
        return northEastAdjacent(charIndex, line, lineIndex, content)
    if (borderType == "southEast"):
        return southEastAdjacent(charIndex, line, lineIndex, content)
    if (borderType == "southWest"):
        return southWestAdjacent(charIndex, line, lineIndex, content)
    if (borderType == "northWest"):
        return northWestAdjacent(charIndex, line, lineIndex, content)
    if (borderType == "north"):
        return northAdjacent(charIndex, line, lineIndex, content)
    if (borderType == "east"):
        return eastAdjacent(charIndex, line, lineIndex, content)
    if (borderType == "south"):
        return southAdjacent(charIndex, line, lineIndex, content)
    if (borderType == "west"):
        return westAdjacent(charIndex, line, lineIndex, content)

    return centralAdjacent(charIndex, line, lineIndex, content)


def getNorthEastAdjacentNumbers(charIndex, line, lineIndex, content):
    adjacentNumbers = []

    westChar = line[charIndex-1]
    if (westChar.isdigit()):
        adjacentNumbers.append(getNumber(westChar, charIndex-1, line))

    southWestChar = content[lineIndex+1][charIndex-1]
    southChar = content[lineIndex+1][charIndex]
    if (southWestChar.isdigit()):
        adjacentNumbers.append(
            getNumber(southWestChar, charIndex-1, content[lineIndex+1]))
    elif (southChar.isdigit()):
        adjacentNumbers.append(
            getNumber(southChar, charIndex, content[lineIndex+1]))

    return adjacentNumbers


def getSouthEastAdjacentNumbers(charIndex, line, lineIndex, content):
    adjacentNumbers = []

    westChar = line[charIndex-1]
    if (westChar.isdigit()):
        adjacentNumbers.append(getNumber(westChar, charIndex-1, line))

    northWestChar = content[lineIndex-1][charIndex-1]
    northChar = content[lineIndex-1][charIndex]
    if (northWestChar.isdigit()):
        adjacentNumbers.append(
            getNumber(northWestChar, charIndex-1, content[lineIndex-1]))
    elif (northChar.isdigit()):
        adjacentNumbers.append(
            getNumber(northChar, charIndex, content[lineIndex-1]))

    return adjacentNumbers


def getSouthWestAdjacentNumbers(charIndex, line, lineIndex, content):
    adjacentNumbers = []

    eastChar = line[charIndex+1]
    if (eastChar.isdigit()):
        adjacentNumbers.append(getNumber(eastChar, charIndex+1, line))

    northEastChar = content[lineIndex-1][charIndex+1]
    northChar = content[lineIndex-1][charIndex]
    if (northEastChar.isdigit()):
        adjacentNumbers.append(
            getNumber(northEastChar, charIndex+1, content[lineIndex-1]))
    elif (northChar.isdigit()):
        adjacentNumbers.append(
            getNumber(northChar, charIndex, content[lineIndex-1]))

    return adjacentNumbers


def getNorthWestAdjacentNumbers(charIndex, line, lineIndex, content):
    adjacentNumbers = []

    eastChar = line[charIndex+1]
    if (eastChar.isdigit()):
        adjacentNumbers.append(getNumber(eastChar, charIndex+1, line))

    southEastChar = content[lineIndex+1][charIndex+1]
    southChar = content[lineIndex+1][charIndex]
    if (southEastChar.isdigit()):
        adjacentNumbers.append(
            getNumber(southEastChar, charIndex+1, content[lineIndex+1]))
    elif (southChar.isdigit()):
        adjacentNumbers.append(
            getNumber(southChar, charIndex, content[lineIndex+1]))

    return adjacentNumbers


def getNorthAdjacentNumbers(charIndex, line, lineIndex, content):
    adjacentNumbers = []

    westChar = line[charIndex-1]
    if (westChar.isdigit()):
        adjacentNumbers.append(getNumber(westChar, charIndex-1, line))

    eastChar = line[charIndex+1]
    if (eastChar.isdigit()):
        adjacentNumbers.append(getNumber(eastChar, charIndex+1, line))

    southChar = content[lineIndex+1][charIndex]
    if (southChar.isdigit()):
        adjacentNumbers.append(
            getNumber(southChar, charIndex, content[lineIndex+1]))
    else:
        southWestChar = content[lineIndex+1][charIndex-1]
        southEastChar = content[lineIndex+1][charIndex+1]
        if (southWestChar.isdigit()):
            adjacentNumbers.append(
                getNumber(southWestChar, charIndex-1, content[lineIndex+1]))
        if (southEastChar.isdigit()):
            adjacentNumbers.append(
                getNumber(southEastChar, charIndex+1, content[lineIndex+1]))

    return adjacentNumbers


def getEastAdjacentNumbers(charIndex, line, lineIndex, content):
    adjacentNumbers = []

    northWestChar = content[lineIndex-1][charIndex-1]
    northChar = content[lineIndex-1][charIndex]
    if (northWestChar.isdigit()):
        adjacentNumbers.append(
            getNumber(northWestChar, charIndex-1, content[lineIndex-1]))
    elif (northChar.isdigit()):
        adjacentNumbers.append(
            getNumber(northChar, charIndex, content[lineIndex-1]))

    southWestChar = content[lineIndex+1][charIndex-1]
    southChar = content[lineIndex+1][charIndex]
    if (southWestChar.isdigit()):
        adjacentNumbers.append(
            getNumber(southWestChar, charIndex-1, content[lineIndex+1]))
    elif (southChar.isdigit()):
        adjacentNumbers.append(
            getNumber(southChar, charIndex, content[lineIndex+1]))

    westChar = line[charIndex-1]
    if (westChar.isdigit()):
        adjacentNumbers.append(getNumber(westChar, charIndex-1, line))

    return adjacentNumbers


def getSouthAdjacentNumbers(charIndex, line, lineIndex, content):
    adjacentNumbers = []

    westChar = line[charIndex-1]
    if (westChar.isdigit()):
        adjacentNumbers.append(getNumber(westChar, charIndex-1, line))

    eastChar = line[charIndex+1]
    if (eastChar.isdigit()):
        adjacentNumbers.append(getNumber(eastChar, charIndex+1, line))

    northChar = content[lineIndex-1][charIndex]
    if (northChar.isdigit()):
        adjacentNumbers.append(
            getNumber(northChar, charIndex, content[lineIndex-1]))
    else:
        northWestChar = content[lineIndex-1][charIndex-1]
        northEastChar = content[lineIndex-1][charIndex+1]
        if (northWestChar.isdigit()):
            adjacentNumbers.append(
                getNumber(northWestChar, charIndex-1, content[lineIndex-1]))
        if (northEastChar.isdigit()):
            adjacentNumbers.append(
                getNumber(northEastChar, charIndex+1, content[lineIndex-1]))

    return adjacentNumbers


def getWestAdjacentNumbers(charIndex, line, lineIndex, content):
    adjacentNumbers = []

    northEastChar = content[lineIndex-1][charIndex+1]
    northChar = content[lineIndex-1][charIndex]
    if (northEastChar.isdigit()):
        adjacentNumbers.append(
            getNumber(northEastChar, charIndex+1, content[lineIndex-1]))
    elif (northChar.isdigit()):
        adjacentNumbers.append(
            getNumber(northChar, charIndex, content[lineIndex-1]))

    southEastChar = content[lineIndex+1][charIndex+1]
    southChar = content[lineIndex+1][charIndex]
    if (southEastChar.isdigit()):
        adjacentNumbers.append(
            getNumber(southEastChar, charIndex+1, content[lineIndex+1]))
    elif (southChar.isdigit()):
        adjacentNumbers.append(
            getNumber(southChar, charIndex, content[lineIndex+1]))

    eastChar = line[charIndex+1]
    if (eastChar.isdigit()):
        adjacentNumbers.append(getNumber(eastChar, charIndex+1, line))

    return adjacentNumbers


def getCentralAdjacentNumbers(charIndex, line, lineIndex, content):
    adjacentNumbers = []

    # check north
    northChar = content[lineIndex-1][charIndex]
    if (northChar.isdigit()):
        adjacentNumbers.append(
            getNumber(northChar, charIndex, content[lineIndex-1]))
    else:
        northWestChar = content[lineIndex-1][charIndex-1]
        northEastChar = content[lineIndex-1][charIndex+1]
        if (northWestChar.isdigit()):
            adjacentNumbers.append(
                getNumber(northWestChar, charIndex-1, content[lineIndex-1]))
        if (northEastChar.isdigit()):
            adjacentNumbers.append(
                getNumber(northEastChar, charIndex+1, content[lineIndex-1]))

    # check east
    eastChar = line[charIndex+1]
    if (eastChar.isdigit()):
        adjacentNumbers.append(getNumber(eastChar, charIndex+1, line))

    # check south
    southChar = content[lineIndex+1][charIndex]
    if (southChar.isdigit()):
        adjacentNumbers.append(
            getNumber(southChar, charIndex, content[lineIndex+1]))
    else:
        southWestChar = content[lineIndex+1][charIndex-1]
        southEastChar = content[lineIndex+1][charIndex+1]
        if (southWestChar.isdigit()):
            adjacentNumbers.append(
                getNumber(southWestChar, charIndex-1, content[lineIndex+1]))
        if (southEastChar.isdigit()):
            adjacentNumbers.append(
                getNumber(southEastChar, charIndex+1, content[lineIndex+1]))

    # check west
    westChar = line[charIndex-1]
    if (westChar.isdigit()):
        adjacentNumbers.append(getNumber(westChar, charIndex-1, line))

    return adjacentNumbers


def getAdjacentNumbers(charIndex, line, lineIndex, content):
    borderType = getBorderType(charIndex, line, lineIndex, content)

    if (borderType == "northEast"):
        return getNorthEastAdjacentNumbers(charIndex, line, lineIndex, content)
    if (borderType == "southEast"):
        return getSouthEastAdjacentNumbers(charIndex, line, lineIndex, content)
    if (borderType == "southWest"):
        return getSouthWestAdjacentNumbers(charIndex, line, lineIndex, content)
    if (borderType == "northWest"):
        return getNorthWestAdjacentNumbers(charIndex, line, lineIndex, content)
    if (borderType == "north"):
        return getNorthAdjacentNumbers(charIndex, line, lineIndex, content)
    if (borderType == "east"):
        return getEastAdjacentNumbers(charIndex, line, lineIndex, content)
    if (borderType == "south"):
        return getSouthAdjacentNumbers(charIndex, line, lineIndex, content)
    if (borderType == "west"):
        return getWestAdjacentNumbers(charIndex, line, lineIndex, content)
    # will always default to central
    return getCentralAdjacentNumbers(charIndex, line, lineIndex, content)


def isGear(char, charIndex, line, lineIndex, content):
    adjacentNumbers = getAdjacentNumbers(charIndex, line, lineIndex, content)
    if (char == "*" and len(adjacentNumbers) == 2):
        return True
    return False

# returns a map


def mapResources(chunk_index, source, destination, rangeLength, resourceMap=null):
    if (resourceMap == null):
        resourceMap = {}

    i = 0
    while i < rangeLength:
        row = []
        row.append(source+i)
        row.append(destination+i)
        resourceMap.append(row)

        i += 1

    return resourceMap
