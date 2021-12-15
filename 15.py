
input = open("15_input").read()

data = [[int(c) for c in l ] for l in input.strip().split("\n")]
maxValue = 100000000
map = [[maxValue for v in l] for l in data]

map[0][0] = data[0][0]

nx = len(data[0])
ny = len(data)

start = (0, 0)
stack = [start]
while stack:
    x, y = stack[-1]
    stack = stack[:-1]
    val = map[y][x]
    if x < nx - 1:
        prevVal = map[y][x + 1]
        newVal = val + data[y][x + 1]
        if newVal < prevVal:
            map[y][x + 1] = newVal
            stack.append((x + 1, y))
    # if x > 0:
    #     prevVal = map[y][x - 1]
    #     newVal = val + data[y][x - 1]
    #     if newVal < prevVal:
    #         map[y][x - 1]
    #         stack.append((x - 1, y))
    if y < ny - 1:
        prevVal = map[y + 1][x]
        newVal = val + data[y + 1][x]
        if newVal < prevVal:
            map[y + 1][x] = newVal
            stack.append((x, y + 1))
    # if y > 0:
    #     prevVal = map[y - 1][x]
    #     newVal = val + data[y - 1][x]
    #     if newVal < prevVal:
    #         map[y - 1][x] = newVal
    #         stack.append((x, y - 1))

print(map[ny - 1][nx - 1] - data[0][0])






input = open("15_input").read()


data = [[int(c) for c in l ] for l in input.strip().split("\n")]
maxValue = 10000000000

onx = len(data[0])
ony = len(data)
nx = 5 * onx
ny = 5 * ony

map = [[maxValue for v in range(nx)] for l in range(ny)]
map[0][0] = data[0][0]

def getVal(x, y):
    ix = x // onx
    iy = y // ony
    px = x % onx
    py = y % ony
    return ((ix + iy) + data[py][px] - 1) % 9 + 1


start = (0, 0)
stack = [start]
while stack:
    x, y = stack[0]
    stack = stack[1:]
    val = map[y][x]
    positions = []
    if x < nx - 1: positions.append((x + 1, y))
    if x > 0: positions.append((x - 1, y))
    if y < ny - 1: positions.append((x, y + 1))
    if y > 0: positions.append((x, y - 1))
    for p in positions:
        prevVal = map[p[1]][p[0]]
        newVal = val + getVal(*p)
        if newVal < prevVal:
            map[p[1]][p[0]] = newVal
            if not(p in stack):
                stack.append(p)

print(map[ny - 1][nx - 1] - data[0][0])

#part1 15min27
#total 1h15
