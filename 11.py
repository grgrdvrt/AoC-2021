input = open("11_input").read()

input1 = """
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""

input2 = """
11111
19991
19191
19991
11111
"""

# input = input1
steps = 100

def printMap(values):
    for l in values:
        print("".join([("  " if i < 10 else " ") + str(i) for i in l]))

def printFlash(values):
    for l in values:
        print("".join([("#" if v else ".") for v in l]))


values = [[int(v) for v in l] for l in input.strip().split("\n")]

def increaseLevels(octos):
    return [[v + 1 for v in l] for l in octos]

def solveFlashes(octos):
    flashes = 0
    flashed = [[False for v in row] for row in octos]
    requireUpdate = True
    while requireUpdate:
        requireUpdate = False
        for j, row in enumerate(octos):
            for i, v in enumerate(row):
                if v > 9:
                    flashes += 1
                    octos[j][i] = 0
                    if not(flashed[j][i]):
                        flashed[j][i] = True
                        if j > 0:
                            if i > 0:
                                octos[j-1][i-1] += 1
                            octos[j-1][i] += 1
                            if i < len(row) - 1:octos[j-1][i+1] += 1
                        if i > 0:
                            octos[j][i-1] += 1
                        if i < len(row) - 1:octos[j][i+1] += 1
                        if j < len(octos) - 1:
                            if i > 0:octos[j+1][i-1] += 1
                            octos[j+1][i] += 1
                            if i < len(row) - 1:octos[j+1][i+1] += 1
        for j, row in enumerate(octos):
            for i, v in enumerate(row):
                if flashed[j][i]:
                    octos[j][i] = 0
        # printMap(octos)
        # printFlash(flashed)
        requireUpdate = any([any([v > 9 for v in row]) for row in octos])
        # print(requireUpdate)
    # printFlash(flashed)
    return (flashes, all([all(r) for r in flashed]))



flashes = 0
for step in range(steps):
    values = increaseLevels(values)
    flashes += solveFlashes(values)[0]
    # print(step)
    # printMap(values)
print(flashes)


step = 0
while True:
    values = increaseLevels(values)
    if solveFlashes(values)[1]:
        print(step + 1)
        break
    step += 1

#part1 35min
#total:39min
