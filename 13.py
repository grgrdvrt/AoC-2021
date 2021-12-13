import re
input = open("13_input").read()

input, foldInfos = input.split("\n\n")

def printPts(pts, w, h):
    for j in range(h + 1):
        line = ""
        for i in range(w + 1):
            line += "#" if (i, j) in pts else "."
        print(line)

pts = [[int(v) for v in l.split(",")] for l in input.strip().split("\n")]
pts = [(pt[0], pt[1]) for pt in pts]
instructions = [re.findall(r"(x|y)=(\d+)", l)[0] for l in foldInfos.strip().split("\n")]
instructions = [(axis, int(v)) for axis, v in instructions]

# print(pts)
# print(instructions)

w = max([pt[0] for pt in pts])
h = max([pt[1] for pt in pts])

print(w, h)

def foldX(pts, x, w, h):
    newPts = set()
    for pt in pts:
        if pt[0] > x:
            newPts.add((2 * x - pt[0], pt[1]))
        else: newPts.add(pt)
    return (newPts, w//2, h)


def foldY(pts, y, w, h):
    newPts = set()
    for pt in pts:
        if pt[1] > y:
            newPts.add((pt[0], 2*y - pt[1]))
        else: newPts.add(pt)
    return (newPts, w, h//2)

print(len(foldX(pts, instructions[0][1], w, h)[0]))

for inst in instructions:
    # printPts(pts, w, h)
    if inst[0] == "x":
        pts, w, h = foldX(pts, inst[1], w, h)
    elif inst[0] == "y":
        pts, w, h = foldY(pts, inst[1], w, h)
    print(inst[0], w, h)


print(w, h)



printPts(pts, w, h)
#part1 11min36s
#total:35min
