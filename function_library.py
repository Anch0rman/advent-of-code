import constants
import math
from shapely.geometry import Polygon, Point


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


# a "configuration" is a - delimited string of card frequencies, sorted in descending order
def get_hand_configuration(hand):
    if len(hand) != 5 or not all(card in constants.CAMEL_CARDS for card in hand):
        return "Invalid hand"

    # count the card frequencies
    card_frequencies = {}
    for card in hand:
        if card not in card_frequencies:
            card_frequencies[card] = 1
        else:
            card_frequencies[card] += 1

    # sort the card frequencies in descending order
    sorted_frequencies = sorted(list(card_frequencies.values()), reverse=True)

    # implode the sorted frequencies into a string
    hand_configuration = '-'.join(str(frequency)
                                  for frequency in sorted_frequencies)

    return hand_configuration


def is_valid_hand_configuration(hand_configuration):
    return hand_configuration in constants.CAMEL_CARD_HAND_CONFIGURATIONS


def get_hand_type(hand_configuration):
    if not is_valid_hand_configuration(hand_configuration):
        return "Invalid hand"

    return constants.CAMEL_CARD_HAND_TYPES[hand_configuration]


def get_type_strength(hand_configuration):
    if not is_valid_hand_configuration(hand_configuration):
        return "Invalid hand"

    return constants.CAMEL_CARD_TYPE_STRENGTHS[hand_configuration]


def compute_hand_strength(hand):
    hand_configuration = get_hand_configuration(hand)
    type_strength = get_type_strength(hand_configuration)

    converted_hand = ""
    for i in range(0, len(hand)):
        converted_hand += constants.CAMEL_CARD_STRENGTHS[hand[i]]

    # print(type_strength + converted_hand)

    return type_strength + converted_hand


def compute_wildcard_hand_strength(hand):
    hand_configuration = get_hand_configuration(hand)
    if "J" in hand:
        num_wildcards = hand.count("J")
        hand_configuration = upgrade_hand_configuration(
            hand_configuration, num_wildcards)
    type_strength = get_type_strength(hand_configuration)

    converted_hand = ""
    for i in range(0, len(hand)):
        converted_hand += constants.CAMEL_CARD_WILDCARD_STRENGTHS[hand[i]]

    # print(type_strength + converted_hand)

    return type_strength + converted_hand


def upgrade_hand_configuration(hand_configuration, num_wildcards):
    # config 5: nothing
    # config 4-1: num_wildcards doesn't matter. best upgrade is config 5
    # config 3-2: num wildcards doesn't matter. best upgrade is config 5
    # config 3-1-1: num_wildcards doesn't matter. best upgrade is 4-1
    # config 2-2-1: if 2 wildcards, best upgrade is 4-1. if 1 wildcard, best upgrade is 3-2
    # config 2-1-1-1: num_wildcards doesn't matter. best upgrade is 3-1-1
    # config 1-1-1-1-1: num_wildcards doesn't  matter. best upgrade is 2-1-1-1
    if hand_configuration == "5":
        return "5"
    if hand_configuration == "4-1":
        return "5"
    if hand_configuration == "3-2":
        return "5"
    if hand_configuration == "3-1-1":
        return "4-1"
    if hand_configuration == "2-2-1":
        if num_wildcards == 2:
            return "4-1"
        if num_wildcards == 1:
            return "3-2"
    if hand_configuration == "2-1-1-1":
        return "3-1-1"
    if hand_configuration == "1-1-1-1-1":
        return "2-1-1-1"


# Function to calculate GCD
def calculate_gcd(x, y):
    while y:
        x, y = y, x % y
    return abs(x)


# Function to calculate LCM
def calculate_lcm(numbers):
    lcm_result = 1
    for number in numbers:
        gcd = calculate_gcd(lcm_result, number)
        lcm_result *= number // gcd
    return lcm_result


def generate_sequence_differences(sequence):
    sequence_differences = []
    for i in range(len(sequence) - 1):
        sequence_differences.append(sequence[i + 1] - sequence[i])

    return sequence_differences


def all_zeroes(sequence):
    for i in sequence:
        if i != 0:
            return False

    return True


def extrapolate_next_value(sequence, last_value_sum):
    if all_zeroes(sequence):
        return last_value_sum

    sequence_differences = generate_sequence_differences(sequence)
    last_value_sum += sequence[len(sequence) - 1]

    return extrapolate_next_value(sequence_differences, last_value_sum)


def get_exit_direction(entrance_direction, pipe_type):
    if pipe_type == 'F':
        if entrance_direction == 'S':
            return 'E'
        elif entrance_direction == 'E':
            return 'S'
    elif pipe_type == 'L':
        if entrance_direction == 'N':
            return 'E'
        elif entrance_direction == 'E':
            return 'N'
    elif pipe_type == 'J':
        if entrance_direction == 'N':
            return 'W'
        elif entrance_direction == 'W':
            return 'N'
    elif pipe_type == '7':
        if entrance_direction == 'S':
            return 'W'
        elif entrance_direction == 'W':
            return 'S'
    elif pipe_type == '|':
        if entrance_direction == 'N':
            return 'S'
        elif entrance_direction == 'S':
            return 'N'
    elif pipe_type == '-':
        if entrance_direction == 'E':
            return 'W'
        elif entrance_direction == 'W':
            return 'E'

    return 'X'  # invalid direction or character


def get_entrance_direction(exit_direction):
    if exit_direction == 'N':
        return 'S'
    elif exit_direction == 'S':
        return 'N'
    elif exit_direction == 'E':
        return 'W'
    elif exit_direction == 'W':
        return 'E'


def get_adjacent_pipe(direction, x, y, content):
    # check valid x and y
    if x < 0 or y < 0:
        return 'X'
    if y >= len(content) or x >= len(content[y]):
        return 'X'

    # check if we're at the edge of the map
    if direction == 'N' and y == 0:
        return 'X'
    if direction == 'S' and y == len(content)-1:
        return 'X'
    if direction == 'E' and x == len(content[y])-1:
        return 'X'
    if direction == 'W' and x == 0:
        return 'X'

    if direction == 'N':
        return content[y-1][x]
    if direction == 'S':
        return content[y+1][x]
    if direction == 'E':
        return content[y][x+1]
    if direction == 'W':
        return content[y][x-1]


def check_direction(direction, x, y, content):
    pipe = get_adjacent_pipe(direction, x, y, content)
    if pipe == 'X':
        return False

    if direction == "N" and (pipe == 'F' or pipe == '7' or pipe == '|'):
        return True
    if direction == "E" and (pipe == '7' or pipe == 'J' or pipe == '-'):
        return True
    if direction == "S" and (pipe == 'J' or pipe == 'L' or pipe == '|'):
        return True
    if direction == "W" and (pipe == 'L' or pipe == 'F' or pipe == '-'):
        return True

    return False


# if there are more pipe forms, we could be at a +, T, left T, right T, inverted T,
# 7, L, J, F, |, -, N, E, S, W
# we could go any direction (N, E, S, W)
# we could go 3 directions (N, E, S), (N, E, W), (N, S, W), (E, S, W)
# we could go 2 directions (N, E), (N, S), (N, W), (E, S), (E, W), (S, W)
# we could go 1 direction aka we're at a dead end (N), (E), (S), (W)
def get_eligible_directions(x, y, content):
    eligible_directions = []

    if check_direction('N', x, y, content):
        eligible_directions.append('N')
    if check_direction('E', x, y, content):
        eligible_directions.append('E')
    if check_direction('S', x, y, content):
        eligible_directions.append('S')
    if check_direction('W', x, y, content):
        eligible_directions.append('W')

    return eligible_directions


def get_next_coordinates(direction, x, y):
    if direction == 'N':
        return x, y-1
    if direction == 'E':
        return x+1, y
    if direction == 'S':
        return x, y+1
    if direction == 'W':
        return x-1, y


def calculate_interior_points(polygon):
    min_x, min_y, max_x, max_y = polygon.bounds
    interior_points = []

    for x in range(int(min_x), int(max_x) + 1):
        for y in range(int(min_y), int(max_y) + 1):
            point = Point(x, y)
            if polygon.contains(point):
                interior_points.append((x, y))

    return interior_points


def has_character(string, character):
    return character in string
