# data = """
# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678"""
data = [[int(v) for v in line] for line in open("09_input").read().strip().split("\n")]
# print(data)

ny = len(data)
nx = len(data[0])

total = 0
for j in range(ny):
    for i in range(nx):
        v = data[j][i]

        minVal = 10
        if j > 0: minVal = min(minVal, data[j - 1][i])
        if j < ny - 1: minVal = min(minVal, data[j + 1][i])
        if i > 0: minVal = min(minVal, data[j][i - 1])
        if i < nx - 1: minVal = min(minVal, data[j][i + 1])

        if v < minVal: total += v + 1
print(total)





# print("\n".join(["".join([str(v) for v in row]) for row in data]))


def getNeighbours(i, j, nx, ny):
    neighbours = []
    if j > 0: neighbours.append((i, j - 1))
    if j < ny - 1: neighbours.append((i, j + 1))
    if i > 0: neighbours.append((i - 1, j))
    if i < nx - 1: neighbours.append((i + 1, j))
    return neighbours

lowPoints = set()
for j in range(ny):
    for i in range(nx):
        v = data[j][i]
        minVal = min([data[p[1]][p[0]] for p in getNeighbours(i, j, nx, ny)])
        if v < minVal:
            lowPoints.add((i, j, v))



def printBasin(basin, data):
    print(basin)
    for j, row in enumerate(data):
        rowStr = ""
        for i, val in enumerate(row):
            rowStr += str(val) if (i, j) in basin else "."
        print(rowStr)


lengths = []

for p in lowPoints:
    basin = set([(p[0], p[1])])
    stack = set([p])
    while stack:
        newStack = set()
        for pos in stack:
            neighbours = getNeighbours(pos[0], pos[1], nx, ny)
            addition = set([p for p in neighbours if data[p[1]][p[0]] < 9]) - basin
            basin |= addition
            newStack |= addition
        stack = newStack
    # printBasin(basin, data)
    lengths.append(len(basin))


# print(lengths)
a, b, c = sorted(lengths)[-3:]
print(a * b * c)

#part1 32min
#total 2h15min
