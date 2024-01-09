import os
import file_reader
from function_library import isAdjacent, isFirstDigit, isLastDigit

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, file_reader.filename)

with open(file_path) as f:
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
        # character iterator. we're assuming every line is the same length
        charIndex = 0
        while charIndex < len(currentLine):
            currentChar = currentLine[charIndex]
            if(currentChar.isdigit()):
                if not numberHasAdjacent:
                    # check if it's adjacent to a symbol
                    numberHasAdjacent = isAdjacent(charIndex, currentLine, lineIndex, content)

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