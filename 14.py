from collections import Counter

input = open("14_input").read()


polymer, pairs = input.strip().split("\n\n")
pairs = [l.strip().split(" -> ") for l in pairs.strip().split("\n")]
pairs = {key:value for key, value in pairs}

for i in range(10):
    newPoly = polymer[0]
    for a, b in zip(polymer, polymer[1:]):
        newPoly += pairs[a+b] + b
    polymer = newPoly

# print(polymer)

quantities = Counter(polymer).values()
print(max(quantities) - min(quantities))

# x < 167010





polymer, pairs = input.strip().split("\n\n")
pairs = [l.strip().split(" -> ") for l in pairs.strip().split("\n")]
pairs = {tuple(key):value for key, value in pairs}

print(polymer)
pairsInPoly = list(zip(polymer, polymer[1:]))
print(pairsInPoly)
count = dict(Counter(pairsInPoly))
print(count)
for i in range(40):
    newCount = {}
    for (p, n) in count.items():
        v = pairs[p]
        p1 = (p[0], v)
        p2 = (v, p[1])
        newCount.setdefault(p1, 0)
        newCount.setdefault(p2, 0)
        newCount[p1] += n
        newCount[p2] += n
    count = newCount

symbols = {}
for (p, v) in count.items():
    symbols.setdefault(p[0], 0)
    symbols[p[0]] += v
    symbols.setdefault(p[1], 0)
    symbols[p[1]] += v

for c, v in symbols.items():
    symbols[c] = v//2

print(polymer[0], polymer[-1])
symbols[polymer[0]] += 1
symbols[polymer[-1]] += 1

quantities = symbols.values()
print(max(quantities) - min(quantities))
# x > 3152788426515
# actual result is 3152788426516, manually corrected

#part1: 8min04
#total: 1h

