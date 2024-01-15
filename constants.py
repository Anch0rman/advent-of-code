CAMEL_CARDS = ["2", "3", "4", "5", "6",
               "7", "8", "9", "T", "J", "Q", "K", "A"]

CAMEL_CARD_STRENGTHS = {
    "2": "0",
    "3": "1",
    "4": "2",
    "5": "3",
    "6": "4",
    "7": "5",
    "8": "6",
    "9": "7",
    "T": "8",
    "J": "9",
    "Q": "A",
    "K": "B",
    "A": "C"
}

CAMEL_CARD_WILDCARD_STRENGTHS = {
    "J": "0",
    "2": "1",
    "3": "2",
    "4": "3",
    "5": "4",
    "6": "5",
    "7": "6",
    "8": "7",
    "9": "8",
    "T": "9",
    "Q": "A",
    "K": "B",
    "A": "C"
}

CAMEL_CARD_HAND_CONFIGURATIONS = [
    "5", "4-1", "3-2", "3-1-1", "2-2-1", "2-1-1-1", "1-1-1-1-1"]

CAMEL_CARD_HAND_TYPES = {
    "5": "five of a kind",
    "4-1": "four of a kind",
    "3-2": "full house",
    "3-1-1": "three of a kind",
    "2-2-1": "two pair",
    "2-1-1-1": "one pair",
    "1-1-1-1-1": "high card"
}

CAMEL_CARD_TYPE_STRENGTHS = {
    "5": "7",
    "4-1": "6",
    "3-2": "5",
    "3-1-1": "4",
    "2-2-1": "3",
    "2-1-1-1": "2",
    "1-1-1-1-1": "1"
}
