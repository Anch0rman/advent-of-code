import os
import file_reader
from function_library import checkStringForMapWord

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, file_reader.filename)

digimon = { 'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9' }

# read in the file
with open(file_path) as f:
    sum = 0
    content = f.readlines()

    # loop through each line, removing the newline character
    for line in content:
        line = line.strip()
        amalgamation1 = ""
        amalgamation2 = ""

        # loop through each character in the line
        for char in line:
            # if the character is a number
            if char.isdigit():
                digit1 = char
                break

            amalgamation1 = amalgamation1 + char
            digit1 = checkStringForMapWord(amalgamation1, digimon)
            
            if digit1:
                break

        # loop backwards through each character in the line
        for char in reversed(line):
            # if the character is a number
            if char.isdigit():
                digit2 = char
                break

            amalgamation2 = char + amalgamation2
            digit2 = checkStringForMapWord(amalgamation2, digimon)

            if digit2:
                break

        # concatenate the two numbers
        num = int(digit1 + digit2)
        sum += num
        print(num, sum)