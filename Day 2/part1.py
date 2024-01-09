import os
import file_reader
import function_library

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, file_reader.filename)

measuringStick = {"red": 12, "green": 13, "blue": 14 }

with open(file_path) as f:
    
    content = f.readlines()
    sum = 0
    # loop through each line
    for line in content:
        line = line.strip()

        game = line.split(":")[0]
        gameValue = game.split(" ")[1]

        cubeSets = line.split(":")[1]
        cubeSetsArray = cubeSets.split(";")
        invalid = False
        for cubeSet in cubeSetsArray:
            if invalid:
                break
            countsAndColors = cubeSet.split(",")

            for countAndColor in countsAndColors:
                countAndColor = countAndColor.strip()
                count = int(countAndColor.split(" ")[0])
                color = countAndColor.split(" ")[1]
                
                if count > measuringStick[color]:
                    invalid = True
                    print("Invalid: " + gameValue)
                    break

        if not invalid:
            print("Valid: " + gameValue)
            sum += int(gameValue)
            print(sum)