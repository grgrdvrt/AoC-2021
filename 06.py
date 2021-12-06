import re

with open("06_input") as file:
    input = [int(v) for v in file.read().strip().split(",")]
    c = {key:input.count(key) for key in set(input)}
    #for i in range(80): #part 1
    for i in range(256):
        c2 = {}
        for j in range(9): c2[j] = 0
        for e in c:
            if e == 0:
                c2[6] += c[e]
                c2[8] += c[e]
            else:
                c2[e - 1] += c[e]
        c = c2


    print(c, sum(c.values()))

# part1: 14min 25s
# total: 14min 55s



#golfed:
with open("06_input") as file:
    input = [int(v) for v in file.read().strip().split(",")]
    c = [input.count(i) for i in range(9)]
    for i in range(256):
        c = c[1:]+[c[0]]
        c[6]+=c[8]
    print(sum(c))
