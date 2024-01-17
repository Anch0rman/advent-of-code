import os
import file_reader
from function_library import extrapolate_next_value

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, file_reader.filename)

with open(file_path) as f:
    content = f.readlines()
    sum = 0

    for line in content:
        sequence = [int(x) for x in line.strip().split(" ")]

        extrapolated_value = extrapolate_next_value(sequence, 0)
        print(extrapolated_value)
        sum += extrapolated_value

    print(sum)
