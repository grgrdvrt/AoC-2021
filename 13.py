import re
input = open("13_input").read()

ptsInput, foldInput = input.strip().split("\n\n")

pts = [tuple([int(v) for v in l.split(",")]) for l in ptsInput.split("\n")]
instructions = [re.findall(r"(x|y)=(\d+)", l)[0] for l in foldInput.split("\n")]
instructions = [(axis, int(v)) for axis, v in instructions]


#part1
# instructions = instructions[:1]

for inst in instructions:
    newPts = set()
    for pt in pts:
        if inst[0] == "x" and pt[0] > inst[1]:
            newPts.add((2 * inst[1] - pt[0], pt[1]))
        elif inst[0] == "y" and pt[1] > inst[1]:
            newPts.add((pt[0], 2*inst[1] - pt[1]))
        else: newPts.add(pt)

    pts = newPts


#part1
print(len(pts))


#part2
w = max([pt[0] for pt in pts])
h = max([pt[1] for pt in pts])
for j in range(h + 1):
    print("".join(["#" if (i, j) in pts else "." for i in range(w + 1)]))

#part1 11min36s
#total:35min
