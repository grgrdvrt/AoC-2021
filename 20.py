input = open("20_input").read();

def padMap(data, val):
    l1 = [val]*(len(data[0]) + 2)
    l2 = [val]*(len(data[0]) + 2)
    return [l1] + [[val] + l + [val] for l in data] + [l2]

def printMap(data):
    for l in data:
        print("".join(["#" if v else "." for v in l]))

def enhance(data, algo, pad):
    result = [[0 for v in l] for l in data]
    for j in range(1, len(data) - 1):
        for i in range(1, len(data[j]) - 1):
            area = [r[i-1:i+2] for r in data[j-1:j+2]]
            val = "".join(["".join([str(v) for v in r]) for r in area])
            index = int(val, 2)
            result[j][i] = algo[index]
    # this is BAD:
    result = [l[1:-1] for l in result[1:-1]]
    return padMap(padMap(result, pad), pad)

algo, data = input.strip().split("\n\n")
algo = [0 if c == "." else 1 for c in algo.strip()]
data = padMap(padMap([[0 if c == "." else 1 for c in l] for l in data.split("\n")], 0), 0)



for i in range(50):
    data = enhance(data, algo, 0 if i%2 else 1)
print(sum([sum(l) for l in data]))
