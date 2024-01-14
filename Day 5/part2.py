import os
import file_reader

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, file_reader.filename)

with open(file_path) as f:
    content = f.readlines()
    seed_range_pairs = content[0].split(":")[1].strip().split(" ")

    # build our seed range tuples
    seed_ranges = []
    for index, seed_range_pair in enumerate(seed_range_pairs):
        if index % 2 == 0:
            seed_start = int(seed_range_pair)
            continue
        else:
            seed_end = seed_start + int(seed_range_pair) - 1
            seed_ranges.append((seed_start, seed_end))

    sorted_seed_ranges = sorted(seed_ranges, key=lambda x: x[0])

    location_value = 0
    while True:
        line_index = len(content) - 1
        carry = location_value
        found_in_chunk = False

        while line_index >= 1:
            line = content[line_index].strip()

            # line is a directive
            if (line and line[0].isdigit() and not found_in_chunk):
                source_start = int(line.split(" ")[0])
                destination_start = int(line.split(" ")[1])
                range_length = int(line.split(" ")[2])
                source_end = source_start + range_length - 1
                range_offset = destination_start - source_start

                if carry >= source_start and carry <= source_end:
                    carry = carry + range_offset
                    found_in_chunk = True

            # end of a chunk of directives
            if not line:
                found_in_chunk = False

            line_index -= 1

        # check if mapped seed is in seed_ranges
        if any(start <= carry < end for start, end in seed_ranges):
            print('location, seed', location_value, carry)
            exit()

        location_value += 1
