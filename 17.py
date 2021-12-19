input = open("17_input").read()

xMin = 150
xMax = 171
yMin = -129
yMax = -70


data = input.strip().split("\n")


def simulate(vx, vy):
    vel = [vx, vy]
    pos = [0, 0]
    i = 10000
    maxY = 0
    while i > 0:
        i -= 1
        pos[0] += vel[0]
        pos[1] += vel[1]
        if vel[0] < 0: vel[0] += 1
        elif vel[0] > 0: vel[0] -= 1
        vel[1] -= 1

        if pos[1] > maxY:
            maxY = pos[1]
        if xMin <= pos[0] <= xMax and yMin <= pos[1] <= yMax:
            return (True, maxY)
        if pos[1] < yMin:
            return (False, 0)
    return (False, 0)

def find():
    vels = set()
    maxY = 0
    for vy in range(-500, 500):
        for vx in range(-500, 200):
            sim = simulate(vx, vy)
            if sim[0]:
                maxY = max(maxY, sim[1])
                vels.add((vx, vy))
                print(len(vels))
    return maxY

print(find())

#29min
#35min
