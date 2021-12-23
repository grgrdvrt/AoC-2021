import re

input = open("22_input").read()


data = input.strip().split("\n")
actions = [1 if l[1] == "n" else 0 for l in data]
print(len(data))

ranges = [[int(v) for v in re.findall(r"-?\d+", l)] for l in data]
bbox = (
    min([v[0] for v in ranges]),
    max([v[1] for v in ranges]),

    min([v[2] for v in ranges]),
    max([v[3] for v in ranges]),

    min([v[4] for v in ranges]),
    max([v[5] for v in ranges])
)

grid = {}

for l, r in enumerate(ranges):
    print("l", actions[l])
    for k in range(max(r[4], -50), min(r[5] + 1, 50)):
        for j in range(max(r[2], -50), min(r[3] + 1, 50)):
            for i in range(max(r[0], -50), min(r[1] + 1, 50)):
                grid.setdefault(k, {})
                grid[k].setdefault(j, {})
                grid[k][j].setdefault(i, {})
                grid[k][j][i] = actions[l]
count = 0
for s in grid:
    for r in grid[s]:
        count += sum(grid[s][r].values())

print(count)

# 669283


def volume(c):
    return (c[1] - c[0] + 1) * (c[3] - c[2] + 1) * (c[5] - c[4] + 1)


def splitCube(a, b):
    if(a[0] > b[1] or
        a[1] < b[0] or
        a[2] > b[3] or
        a[3] < b[2] or
        a[4] > b[5] or
        a[5] < b[4]):return [a]
    x1 = max(a[0], b[0])
    x2 = min(a[1], b[1])
    y1 = max(a[2], b[2])
    y2 = min(a[3], b[3])
    z1 = max(a[4], b[4])
    z2 = min(a[5], b[5])

    subCubes = [
        (a[0], x1 - 1, a[2], a[3], a[4], a[5]),
        (x2 + 1, a[1], a[2], a[3], a[4], a[5]),
        (x1, x2, a[2], y1 - 1, a[4], a[5]),
        (x1, x2, y2 + 1, a[3], a[4], a[5]),
        (x1, x2, y1, y2, a[4], z1 - 1),
        (x1, x2, y1, y2, z2 + 1, a[5])
    ]
    return [c for c in subCubes if volume(c) > 0]


offCubes = [bbox]
print(len(ranges))
for i, c1 in enumerate(ranges):
    newOffCubes = []
    for c2 in offCubes:
        newOffCubes += splitCube(c2, c1)
    if not(actions[i]):
        newOffCubes.append(c1)
    offCubes = newOffCubes
print(volume(bbox) - sum([volume(c) for c in offCubes]))

#part1 30min
#total 1h40
