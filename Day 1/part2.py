digimon = { 'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9' }

def checkStringForMapWord(inputString, map, checkKeys = True):
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
            
            j+=1
            k+=1
        
        i+=1
    
    return False

# read in the file
with open("input.txt") as f:
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