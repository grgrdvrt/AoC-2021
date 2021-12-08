def processLine(line):
    return line.strip().split("|")[1].strip().split(" ")

input = [processLine(line) for line in open("08_input").readlines()]
count = {2:0, 4:0, 3:0, 7:0}
for line in input:
    lengths = [len(w) for w in line]
    print(line, lengths)
    for key in count:
        count[key] += lengths.count(key)
# print(count)
print(count)
result = 0
for v in count:
    result += count[v]
print(result)

# x > 400




def processLine(line):
    parts = line.strip().split("|")
    return [p.strip().split(" ") for p in parts]

input = [processLine(line) for line in open("08_input").readlines()]
total = 0
for line in input:
    sets = [set(w) for w in line[0]]
    v1 = [x for x in sets if len(x) == 2][0]
    v4 = [x for x in sets if len(x) == 4][0]
    v7 = [x for x in sets if len(x) == 3][0]
    v8 = [x for x in sets if len(x) == 7][0]

    # print(v1, v4, v7, v8)

    v352 = [x for x in sets if len(x) == 5]
    v690 = [x for x in sets if len(x) == 6]
    # print(v352)

    v3 = [x for x in v352 if v1 <= x][0]
    v5 = [x for x in v352 if (v4 - v1) <= x][0]
    v2 = [x for x in v352 if not(x in [v3, v5])][0]
    # print(v3, v5, v2)

    v6 = [x for x in v690 if not(v1 <= x)][0]
    v9 = [x for x in v690 if v3 <= x][0]
    v0 = [x for x in v690 if not(x in [v6, v9])][0]
    # print(v6, v9, v0)
    numbers = [v0, v1, v2, v3, v4, v5, v6, v7, v8, v9]
    n = [numbers.index(v) for v in [set(w) for w in line[1]]]
    # print(n)
    total += 1000 * n[0] + 100 * n[1] + 10 * n[2] + n[3]
print(total)

#part1: 7min53
#total: 34min 32
