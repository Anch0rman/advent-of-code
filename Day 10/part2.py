import os
import file_reader
from function_library import get_eligible_directions, get_adjacent_pipe, get_entrance_direction
from function_library import get_exit_direction, get_next_coordinates, calculate_interior_points
from shapely.geometry import Polygon, Point
import matplotlib.pyplot as plt


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

    coordinates = []
    coordinates.append((start_X, start_Y))
    eligible_directions = get_eligible_directions(start_X, start_Y, content)
    current_pipe = get_adjacent_pipe(eligible_directions[0],
                                     start_X, start_Y, content)
    entrance_direction = get_entrance_direction(eligible_directions[0])
    x, y = get_next_coordinates(eligible_directions[0], start_X, start_Y)
    exit_direction = get_exit_direction(entrance_direction, current_pipe)
    coordinates.append((x, y))

    while current_pipe != "S":
        current_pipe = get_adjacent_pipe(exit_direction, x, y, content)
        entrance_direction = get_entrance_direction(exit_direction)
        x, y = get_next_coordinates(exit_direction, x, y)
        exit_direction = get_exit_direction(entrance_direction, current_pipe)
        coordinates.append((x, y))

    polygon = Polygon(coordinates)
    interior_points = calculate_interior_points(polygon)
    print(len(interior_points))
