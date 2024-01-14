import os
import file_reader

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, file_reader.filename)

with open(file_path) as f:
    content = f.readlines()

    time = content[0].strip().replace(" ", "").split(":")[1]
    distance = content[1].strip().replace(" ", "").split(":")[1]
    print(time, distance)

    num_winners = []
    int_time = int(time)
    record_distance = int(distance)
    winner_count = 0

    for i in range(int_time + 1):
        possible_distance = i * (int_time - i)

        if possible_distance > record_distance:
            winner_count += 1

    num_winners.append(winner_count)

    product = 1
    for winner in num_winners:
        product *= winner

    print(product)
