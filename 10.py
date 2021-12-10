data = open("10_input").read()
# print(data)


scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
pairs = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}


score = 0
for l in data.strip().split("\n"):
    stack = []
    for char in l:
        if char in ["(", "[", "{", "<"]:
            stack.append(char)
        else:
            # print(char, stack, stack[-1])
            if not stack or stack[-1] != pairs[char]:
                # print(char)
                score += scores[char]
                break
            elif stack[-1] == pairs[char]:
                stack = stack[:-1]
print(score)


scores = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}


incompleteLines = []
for l in data.strip().split("\n"):
    stack = []
    isValid = True
    for char in l:
        if char in ["(", "[", "{", "<"]:
            stack.append(char)
        else:
            # print(char, stack, stack[-1])
            if not stack or stack[-1] != pairs[char]:
                isValid = False
                break
            elif stack[-1] == pairs[char]:
                stack = stack[:-1]
    if isValid:
        incompleteLines.append(stack)
totalScores =[]
for l in incompleteLines:
    # print(l)
    score = 0
    for char in reversed(l):
        score = 5 * score + scores[char]
    totalScores.append(score)
totalScores = sorted(totalScores)
print(totalScores)
print(totalScores[len(totalScores)//2])

#part1: 7min 18s
#total: 17min 18s
