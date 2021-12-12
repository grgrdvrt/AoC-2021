
input = open("12_input").read()

_input = """
start-A
start-b
A-c
A-b
b-d
A-end
b-end

"""

values = [v.split("-") for v in input.strip().split("\n")]

majs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


nodeNames = set([v[0] for v in values] + [v[1] for v in values])
graph = {}
for name in nodeNames:
    graph[name] = {
        "name":name,
        "neighbours":{},
        "isBig":name[0] in majs
    }

for l in values:
    graph[l[0]]["neighbours"][l[1]] = graph[l[1]]
    graph[l[1]]["neighbours"][l[0]] = graph[l[0]]
closedPaths = set()
stack = [[graph["start"]]]
while stack:
    # print("_____________")
    # for p in stack:
    #     print([n["name"] for n in p])
    path = stack[0]
    nextStack = stack[1:]
    for node in path[-1]["neighbours"].values():
        newPath = [n for n in path]
        if node["isBig"] or not(node in path):
            newPath += [node]
            if node["name"] == "end":
                closedPaths.add(tuple([n["name"] for n in newPath]))
            else:
                nextStack.append(newPath)
    stack = nextStack
print("done")
# for l in closedPaths:
#     print(l)
print(len(closedPaths))







graph = {}
for name in nodeNames:
    graph[name] = {
        "name":name,
        "neighbours":{},
        "isBig":name[0] in majs
    }
from collections import Counter
def hasDouble(path):
    return max(Counter([name for name in path if not(name[0] in majs)]).values()) >= 2

for l in values:
    graph[l[0]]["neighbours"][l[1]] = graph[l[1]]
    graph[l[1]]["neighbours"][l[0]] = graph[l[0]]
closedPaths = set()
stack = [["start"]]

while stack:
    # print("_____________", [p for p in closedPaths if len(p) > 20])
    # for p in stack:
    #     print([n["name"] for n in p])
    path = stack[0]
    nextStack = stack[1:]
    for node in graph[path[-1]]["neighbours"].values():
        if node["name"] == "start":continue
        newPath = [n for n in path]
        if(
                node["isBig"]
                or not(node["name"] in path)
                or not(hasDouble(path))
        ):
            newPath += [node["name"]]
            if node["name"] == "end":
                closedPaths.add(tuple(newPath))
            else:
                nextStack.append(newPath)
    stack = nextStack
print("done")
# for l in closedPaths:
#     print(l)
print(len(closedPaths))


#part1: 56min21
#total: 1h31
