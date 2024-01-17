import os
import file_reader

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, file_reader.filename)

with open(file_path) as f:
    content = f.readlines()
    directions = content[0].strip()
    num_directions = len(directions)

    nodes = {}
    for line in content[2:]:
        node = line.split("=")[0].strip()
        coords = line.split("=")[1].strip().strip("()").split(",")
        left = coords[0].strip()
        right = coords[1].strip()
        nodes[node] = tuple([left, right])

    current_node = "AAA"
    node_coords = nodes[current_node]
    num_steps = 0
    direction_index = 0
    while current_node != "ZZZ":
        direction = directions[direction_index % num_directions]

        if direction == "L":
            current_node = nodes[current_node][0]
            node_coords = nodes[current_node]
        elif direction == "R":
            current_node = nodes[current_node][1]
            node_coords = nodes[current_node]

        num_steps += 1
        direction_index += 1

    print(num_steps)
