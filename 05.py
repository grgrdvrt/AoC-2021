import re


def processLine(line):
    return [int(t) for t in re.findall("(\d+),(\d+) -> (\d+),(\d+)", line.strip())[0]]

def printMap(m):
    for j in range(10):
        l = ""
        for i in range(10):
            if (i, j) in m:l += str(m[(i, j)])
            else:l += "."
        print(l)


with open("input") as file:
    input = [processLine(line) for line in file]
    m = {}
    for l in input:
        if l[0] != l[2] and l[1] != l[3]: continue
        x1 = min(l[0], l[2])
        x2 = max(l[0], l[2])
        y1 = min(l[1], l[3])
        y2 = max(l[1], l[3])
        for j in range(x1, x2 + 1):
            for i in range(y1, y2 + 1):
                m.setdefault((i, j), 0)
                m[(i, j)] += 1

    # printMap(m)
    print(sum([1 if v > 1 else 0 for v in m.values()]))


def sign(x):
    if x < 0: return -1
    elif x > 0: return 1
    else:return 0

with open("input") as file:
    input = [processLine(line) for line in file]
    m = {}
    for l in input:
        dx = l[2] - l[0]
        dy = l[3] - l[1]
        sx = sign(dx)
        sy = sign(dy)
        for i in range(max(abs(dx), abs(dy)) + 1):
            x = l[0] + i * sx
            y = l[1] + i * sy
            m.setdefault((x, y), 0)
            m[(x, y)] += 1


    # printMap(m)
    print(sum([1 if v > 1 else 0 for v in m.values()]))


#part1: 13min 35s
#total: 27min 40s
