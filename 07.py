input = [int(v) for v in open("07_input").read().strip().split(",")]
# input = [16,1,2,0,4,2,7,1,2,14]
results = []
for i in range(min(input), max(input) + 1):
    results.append(sum([abs(i - x) for x in input]))
print(min(results))

results = []
for i in range(min(input), max(input) + 1):
    results.append(sum([((abs(i - x) * (abs(i - x) + 1)) / 2) for x in input]))
print(min(results))

# part1 4min 50
# total 7min

