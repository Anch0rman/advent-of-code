import sys

if(sys.argv[1]):
    filename = sys.argv[1]
else:
    print("No filename provided")
    exit()

with open(filename) as f:
    
    content = f.readlines()
    sum = 0
    # loop through each line
    for line in content:
        line = line.strip()

        game = line.split(":")[0]
        gameValue = game.split(" ")[1]

        # what if we never pull one of the colors?
        # the value would be 0, and then the power would be 0
        powerMap = {"red": 0, "green": 0, "blue": 0 }
        cubeSets = line.split(":")[1]
        cubeSetsArray = cubeSets.split(";")
        for cubeSet in cubeSetsArray:
            countsAndColors = cubeSet.split(",")

            for countAndColor in countsAndColors:
                countAndColor = countAndColor.strip()
                count = int(countAndColor.split(" ")[0])
                color = countAndColor.split(" ")[1]

                if count > powerMap[color]:
                    powerMap[color] = count
        
        setPower = powerMap["red"] * powerMap["green"] * powerMap["blue"]
        sum += setPower
        print(gameValue, powerMap, setPower, sum)