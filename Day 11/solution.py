import os
import file_reader
import sys
from function_library import has_character

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, file_reader.filename)
try:
    multiplier = int(sys.argv[2]) - 1
except IndexError:
    print("Please provide the expansion multiplier")
    exit()

with open(file_path) as f:
    content = f.readlines()
    transposed_content = zip(*content)
    galaxyless_rows = []
    galaxyless_columns = []
    galaxy_coordinates = []
    distances = []
    expanded_distances = []
    sum_distances = 0
    sum_expanded_distances = 0

    # find all rows without a galaxy
    for line_index, line in enumerate(content):
        if not has_character(line.strip(), "#"):
            galaxyless_rows.append(line_index)

    # find all columns without a galaxy
    for column_index, column in enumerate(transposed_content):
        if not has_character(column, "#"):
            galaxyless_columns.append(column_index)

    # find the coordinates of all galaxies
    for line_index, line in enumerate(content):
        for character_index, character in enumerate(line):
            if character == "#":
                galaxy_coordinates.append((line_index, character_index))

    # compare all of the galaxies to each other
    for slow_pointer, galaxy1 in enumerate(galaxy_coordinates):
        for fast_pointer, galaxy2 in enumerate(galaxy_coordinates):
            if fast_pointer > slow_pointer:
                num_galaxyless_vectors_crossed = 0
                y1 = galaxy1[0] if galaxy1[0] < galaxy2[0] else galaxy2[0]
                y2 = galaxy1[0] if galaxy1[0] >= galaxy2[0] else galaxy2[0]
                x1 = galaxy1[1] if galaxy1[1] < galaxy2[1] else galaxy2[1]
                x2 = galaxy1[1] if galaxy1[1] >= galaxy2[1] else galaxy2[1]
                distance = (y2 - y1) + (x2 - x1)
                distances.append(distance)
                sum_distances += distance

                for i in range(y1+1, y2):
                    if i in galaxyless_rows:
                        num_galaxyless_vectors_crossed += 1

                for i in range(x1+1, x2):
                    if i in galaxyless_columns:
                        num_galaxyless_vectors_crossed += 1

                expansion_space = num_galaxyless_vectors_crossed * multiplier
                expanded_distance = distance + expansion_space
                expanded_distances.append(expanded_distance)
                sum_expanded_distances += expanded_distance

    print(sum_expanded_distances)
