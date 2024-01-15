import os
import file_reader
from function_library import compute_wildcard_hand_strength

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, file_reader.filename)

with open(file_path) as f:
    content = f.readlines()
    hand_bid_dict = {}

    for line in content:
        hand = line.strip().split(" ")[0]
        bid = line.strip().split(" ")[1]

        hand_bid_dict[hand] = bid

    # Sorting hands using the custom comparison function
    sorted_list = sorted(list(hand_bid_dict.keys()),
                         key=compute_wildcard_hand_strength)

    sum = 0
    for rank, hand in enumerate(sorted_list):
        rank += 1
        bid = int(hand_bid_dict[hand])

        print(rank, hand, bid, rank * bid)
        sum += rank * bid

    print(sum)
