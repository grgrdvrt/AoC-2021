input = open("12_input").read()

connections = {}
for l in input.strip().split("\n"):
    pair = l.split("-")
    connections.setdefault(pair[0], [])
    connections[pair[0]].append(pair[1])

    connections.setdefault(pair[1], [])
    connections[pair[1]].append(pair[0])


#part1
closedPaths = set()
stack = [["start"]]
while stack:
    path, nextStack = stack[-1], stack[:-1]
    for node in connections[path[-1]]:
        newPath = [n for n in path]
        if node[0].isupper() or not(node in path):
            newPath += [node]
            if node == "end":
                closedPaths.add(tuple(newPath))
            else:
                nextStack.append(newPath)
    stack = nextStack
print(len(closedPaths))




#part2
def hasDouble(path):
    return max([path.count(v) for v in set(path) if not(v[0].isupper())]) >= 2

closedPaths = set()
stack = [["start"]]

while stack:
    path = stack[0]
    nextStack = stack[1:]
    for node in connections[path[-1]]:
        if node == "start":continue
        newPath = [n for n in path]
        if(
                node[0].isupper()
                or not(node in path)
                or not(hasDouble(path))
        ):
            newPath += [node]
            if node == "end":
                closedPaths.add(tuple(newPath))
            else:
                nextStack.append(newPath)
    stack = nextStack
print(len(closedPaths))


#part1: 56min21
#total: 1h31
