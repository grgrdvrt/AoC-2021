p1 = 9
p2 = 3

s1 = 0
s2 = 0

die = [1, 0]

def getVal(die):
    val = die[0]
    die[1] += 1
    die[0] += 1
    if die[0] > 100: die[0] = 1
    return val


while True:
    p1 = (p1 + sum([getVal(die) for i in range(3)]) - 1) % 10 + 1
    s1 += p1
    if s1 >= 1000:break
    p2 = (p2 + sum([getVal(die) for i in range(3)]) - 1) % 10 + 1
    s2 += p2
    if s2 >= 1000:break

print(min(s1, s2) * die[1])



universes = {
    ((9, 0), (3, 0)):1
}


outcomes = [
    (3, 1),
    (4, 3),
    (5, 6),
    (6, 7),
    (7, 6),
    (8, 3),
    (9, 1),
]

t1 = 0
t2 = 0

while len(universes):
    newUniverses = {}
    for val, count in outcomes:
        for state in universes:
            pos, score = state[0]
            newPos = (pos + val - 1) % 10 + 1
            newState = ((newPos, score + newPos), state[1])
            newUniverses.setdefault(newState, 0)
            newUniverses[newState] += count * universes[state]

    universes = newUniverses
    toRemove = []
    for state in universes:
        if state[0][1] >= 21:
            t1 += universes[state]
            toRemove.append(state)
    for state in toRemove:del universes[state]

    newUniverses = {}
    for val, count in outcomes:
        for state in universes:
            pos, score = state[1]
            newPos = (pos + val - 1) % 10 + 1
            newState = (state[0], (newPos, score + newPos))
            newUniverses.setdefault(newState, 0)
            newUniverses[newState] += count * universes[state]
    universes = newUniverses
    toRemove = []
    for state in universes:
        if state[1][1] >= 21:
            t2 += universes[state]
            toRemove.append(state)
    for state in toRemove:del universes[state]

print(max(t1, t2))



# part1 15min
#total 1h30
