# check the 4 directions at S
# can go west if character is F or L
# can go south if character is L or J
# can go east if character is J or 7
# can go north if character is 7 or F

# once a direction is determined, check the character
# we need to know entered direction
# if F, and entered is South, go East
# if F, and entered is East, go South
# if L, and entered is North, go East
# if L, and entered is East, go North
# if J, and entered is North, go West
# if J, and entered is West, go North
# if 7, and entered is South, go West
# if 7, and entered is West, go South

import os
import file_reader
from function_library import get_eligible_directions, get_adjacent_pipe, get_entrance_direction
from function_library import get_exit_direction, get_next_coordinates


script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, file_reader.filename)

with open(file_path) as f:
    content = f.readlines()

    # find S. we're assuming every line is the same length
    for line_index, line in enumerate(content):

        if "S" in line:
            start_Y = line_index
            start_X = line.index("S")
            break

    eligible_directions = get_eligible_directions(start_X, start_Y, content)
    current_pipe = get_adjacent_pipe(eligible_directions[0],
                                     start_X, start_Y, content)
    entrance_direction = get_entrance_direction(eligible_directions[0])
    x, y = get_next_coordinates(eligible_directions[0], start_X, start_Y)
    exit_direction = get_exit_direction(entrance_direction, current_pipe)
    num_steps = 1
    print(current_pipe, entrance_direction, exit_direction, y, x, num_steps)

    while current_pipe != "S":
        current_pipe = get_adjacent_pipe(exit_direction, x, y, content)
        entrance_direction = get_entrance_direction(exit_direction)
        x, y = get_next_coordinates(exit_direction, x, y)
        exit_direction = get_exit_direction(entrance_direction, current_pipe)
        num_steps += 1
        print(current_pipe, entrance_direction,
              exit_direction, y, x, num_steps)

    print(num_steps / 2)
