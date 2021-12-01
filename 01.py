with open("01_input") as file:
    input = [int(line) for line in file]

    #part 1
    print(sum(a < b for (a, b) in zip(input[:-1], input[1:])))

    #part 2
    sums = [sum(input[i:i+3]) for i, v in enumerate(input[:-2])]
    print(sum(a < b for (a, b) in zip(sums[:-1], sums[1:])))
