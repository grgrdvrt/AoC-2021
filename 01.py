"""Original code"""
# part 1
with open("01_input") as file:
    input = [int(line) for line in file]
    count = 0
    prev = input[0]
    for i in range(len(input) - 1):
        if prev < input[i]:
            count += 1
        prev = input[i]
    print(count)

#part 2
with open("01_input") as file:
    input = [int(line) for line in file]

    count = 0
    for i in range(len(input) - 3):
        s1 = sum(input[i:i+3])
        s2 = sum(input[i+1:i+4])
        if s1 < s2:
            count += 1
    print(count)

#part 1: 3min 30
#total: 6min 45




"""golfed"""
with open("01_input") as file:
    input = [int(line) for line in file]

    #part 1
    print(sum(a < b for (a, b) in zip(input[:-1], input[1:])))

    #part 2
    # if a + b + c < b + c + d then a < d
    print(sum(a < b for (a, b) in zip(input[:-3], input[3:])))

