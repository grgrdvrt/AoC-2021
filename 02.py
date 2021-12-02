def processLine(line):
    return line.strip().split(" ")

#part1
pos = [0, 0]
with open("02_input") as file:
    input = [processLine(line) for line in file]
    for l in input:
        if(l[0] == "forward"):
            pos[0] += int(l[1])
        elif(l[0] == "up"):
            pos[1] -= int(l[1])
        elif(l[0] == "down"):
            pos[1] += int(l[1])
    print(pos[0] * pos[1])


#part2
aim = 0
pos = [0, 0]
with open("02_input") as file:
    input = [processLine(line) for line in file]
    for l in input:
        if(l[0] == "down"):
            aim += int(l[1])
        elif(l[0] == "up"):
            aim -= int(l[1])
        elif(l[0] == "forward"):
            pos[0] += int(l[1])
            pos[1] += aim * int(l[1])
    print(pos[0] * pos[1])

#time
#part 1: not logged, ~1min30
#part 2: 3min
#total: ~5min
