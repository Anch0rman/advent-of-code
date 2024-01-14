import os
import file_reader

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, file_reader.filename)

with open(file_path) as f:
    content = f.readlines()

    times = content[0].split(":")[1].strip().split(" ")
    times = [time for time in times if time != '']

    distances = content[1].split(":")[1].strip().split(" ")
    distances = [distance for distance in distances if distance != '']

    records = {}
    for index, time in enumerate(times):
        records[time] = distances[index]

    num_winners = []
    for time in records:
        int_time = int(time)
        record_distance = int(records[time])
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
