# part 1
with open("03_input") as file:
    input = [line.strip() for line in file]
    transposed = list(map(list, zip(*input)))
    a = [max(set(l), key=l.count) for l in transposed]
    b = [min(set(l), key=l.count) for l in transposed]
    print(int("".join(a), 2) * int("".join(b), 2))


# part 2
with open("03_input") as file:
    input = [line.strip() for line in file]

    data = input;
    for i in range(len(input[0])):
        transposed = list(map(list, zip(*data)))
        s = ""
        for l in transposed:
            z, o = l.count("0"), l.count("1")
            s += "0" if z > o else "1"
        data = list(filter(lambda x: x[i] == s[i], data))
        if len(data) == 1:
            ra = data[0]
            break
    # print(ra)
    data = input;
    for i in range(len(input[0])):
        transposed = list(map(list, zip(*data)))
        s = ""
        for l in transposed:
            z, o = l.count("0"), l.count("1")
            s += "0" if z <= o else "1"
        print(s)
        data = list(filter(lambda x: x[i] == s[i], data))
        if len(data) == 1:
            rb = data[0]
            break
    print(rb)
    print(int(ra, 2) * int(rb, 2))




# part 2, rewritten
def computeRate(data, a, b):
    data = input;
    i = 0
    while len(data) > 1:
        transposed = list(map(list, zip(*data)))
        s = [a if l.count("0") > l.count("1") else b for l in transposed]
        data = list(filter(lambda x: x[i] == s[i], data))
        i += 1
    return int(data[0], 2)


with open("03_input") as file:
    input = [line.strip() for line in file]
    print(computeRate(input, "0", "1") * computeRate(input, "1", "0"))
