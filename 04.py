import re

#part1
def isTableComplete(t):
    return any(not(any(l)) for l in t)

def isTableComplete2(t):
    return isTableComplete(t) or isTableComplete(zip(*t))

def tableScore(t):
    return sum([sum([int(v) if v else 0 for v in l]) for l in t])

def processLine(line):
    return re.findall(r"\d+", line.strip())

#part 1
def play():
    with open("04_input") as file:
        data = file.read().split("\n\n")
        vals = data[0].split(",")
        tables = [[processLine(l) for l in t.strip().split("\n")] for t in data[1:]]
        for v in vals:
            for t in tables:
                for j, r in enumerate(t):
                    for i, x in enumerate(r):
                        # print(i, j, v, x)
                        if x and x == v:
                            t[j][i] = False
                            if(isTableComplete2(t)):
                                print(int(v) * tableScore(t))
                                return

play()


#part 2
visited = []
with open("04_input") as file:
    data = file.read().split("\n\n")
    vals = data[0].split(",")
    tables = [[processLine(l) for l in t.strip().split("\n")] for t in data[1:]]
    for v in vals:
        for t in tables:
            for j, r in enumerate(t):
                for i, x in enumerate(r):
                    if x and x == v:
                        t[j][i] = False
                        if(isTableComplete2(t)):
                            if(not t in visited):
                                print(int(v) * tableScore(t))
                                visited.append(t)


#part 1: 20min 33s
#total: 24min 40s
