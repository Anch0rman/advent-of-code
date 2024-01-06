# disclaimer: we don't know that each line is guaranteed to have a digit

# read in the file
with open("input.txt") as f:
    sum = 0
    content = f.readlines()
    # loop through each line
    for line in content:
        # loop through each character in the line
        for char in line:
            # if the character is a number
            if char.isdigit():
                digit1 = char
                break
        # loop backwards through each character in the line
        for char in reversed(line):
            # if the character is a number
            if char.isdigit():
                digit2 = char
                break

        # concatenate the two numbers
        num = int(digit1 + digit2)
        sum += num
        print(sum)