import os
import file_reader
from function_library import getAdjacentNumbers

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
        # character iterator. we're assuming every line has the same length
        charIndex = 0
        while charIndex < len(currentLine):
            currentChar = currentLine[charIndex]
            if(currentChar == "*"):
                adjacentNumbers = getAdjacentNumbers(charIndex, currentLine, lineIndex, content)
                if(len(adjacentNumbers) == 2):
                    # multiply the values
                    gearRatio = int(adjacentNumbers[0]) * int(adjacentNumbers[1])
                    sum += gearRatio
                    print(currentChar, adjacentNumbers, gearRatio, sum)

            charIndex += 1
        lineIndex += 1