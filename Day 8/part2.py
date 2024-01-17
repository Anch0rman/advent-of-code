import os
import file_reader
from function_library import calculate_lcm

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, file_reader.filename)

with open(file_path) as f:
    content = f.readlines()
    directions = content[0].strip()
    num_directions = len(directions)

    # transform the input into a dataset we can process
    nodes = {}
    for line in content[2:]:
        node = line.split("=")[0].strip()
        coords = line.split("=")[1].strip().strip("()").split(",")
        left = coords[0].strip()
        right = coords[1].strip()
        nodes[node] = tuple([left, right])

    # get the nodes that end with "A"
    current_node_set = []
    for node in nodes:
        if node[2] == "A":
            current_node_set.append(node)

    min_steps = []
    # determine the number of steps for each "A" node to reach a "Z" node
    for node in current_node_set:
        current_node = node
        num_steps = 0
        direction_index = 0
        while not current_node.endswith("Z"):
            direction = directions[direction_index % num_directions]

            if direction == "L":
                current_node = nodes[current_node][0]
            elif direction == "R":
                current_node = nodes[current_node][1]

            num_steps += 1
            direction_index += 1

        min_steps.append(num_steps)
        print(node, num_steps, current_node)

    # calculate the LCM of the set of steps
    print(calculate_lcm(min_steps))
