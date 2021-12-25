input = open("input").read()

data = input.strip().split("\n")

def step(data):
    nx = len(data[0])
    ny = len(data)
    newData = [["." for c in l] for l in data]
    moved = False
    for j, l in enumerate(data):
        for i, c in enumerate(l):
            right = 0 if i == nx - 1 else i + 1
            if c == ">" and data[j][right] == ".":
                newData[j][right] = c
                moved = True
            elif c != ".":
                newData[j][i] = c
    data = newData
    newData = [["." for c in l] for l in data]
    for j, l in enumerate(data):
        for i, c in enumerate(l):
            down = 0 if j == ny - 1 else j + 1
            if c == "v" and data[down][i] == ".":
                newData[down][i] = c
                moved = True
            elif c != ".":
                newData[j][i] = c
    return (moved, newData)
  
i = 0
moved = True
while moved:
    i += 1
    moved, data = step(data)
print(i)

#25min
