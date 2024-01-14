import os
import file_reader

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, file_reader.filename)

with open(file_path) as f:
    content = f.readlines()
    seeds = content[0].split(":")[1].strip().split(" ")
    locations = []

    for seed in seeds:
        print('seed', seed)
        line_index = 2
        carry = int(seed)
        found_in_chunk = False

        while line_index < len(content):
            line = content[line_index].strip()

            # line is a directive
            if (line and line[0].isdigit() and not found_in_chunk):
                source_start = int(line.split(" ")[1])
                destination_start = int(line.split(" ")[0])
                range_length = int(line.split(" ")[2])
                source_end = source_start + range_length - 1
                range_offset = destination_start - source_start

                if carry >= source_start and carry <= source_end:
                    carry = carry + range_offset
                    found_in_chunk = True

            # end of a chunk of directives
            if not line or line_index == len(content)-1:
                found_in_chunk = False
                print(carry)

            line_index += 1

        print('location', carry)
        locations.append(carry)

    print(locations)
    print(min(locations))
