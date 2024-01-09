import sys

try:
    filename = sys.argv[1]
except IndexError:
    print("No input filename provided")
    exit()