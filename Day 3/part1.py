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
            if(currentChar.isdigit()):
                if not numberHasAdjacent:
                    # get the border type
                    borderType = getBorderType(currentChar, charIndex, currentLine, lineIndex, content)
                    # check if it's adjacent to a symbol
                    numberHasAdjacent = isAdjacent(borderType, currentChar, charIndex, currentLine, lineIndex, content)

                if(isFirstDigit(currentChar, currentLine, charIndex)):
                    numberStartIndex = charIndex
                if(isLastDigit(currentChar, currentLine, charIndex) and numberHasAdjacent):
                    # we have a number
                    numberEndIndex = charIndex
                    number = currentLine[numberStartIndex:numberEndIndex+1]
                    numberHasAdjacent = False
                    sum += int(number)
                    print(number, sum)

            charIndex += 1
        lineIndex += 1