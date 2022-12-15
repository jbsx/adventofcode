#!/usr/bin/python3
lines = [i.strip().split(" -> ") for i in open("inputday14", "r").readlines()]
input = []

for y in range(len(lines)):
    lines[y] = list(lines[y])
    temp = []
    for j in range(len(lines[y])):
        temp.append([int(i) for i in lines[y][j].split(",")])
    input.append(temp)

l, h, maxheight = float('inf'), 0, 0
for j in input:
    for j in j:
        l = min(l, j[0])
        h = max(h, j[0])
        maxheight = max(maxheight, j[1])
offsetx = int(h - l)

state = [[" " for _ in range(offsetx + 1)] for _ in range(maxheight + 1)]

#PRINT WALLS
for i in input:
    for j in range(1, len(i)):
        fx, fy = i[j - 1][0] - l, i[j - 1][1]
        tx, ty = i[j][0] - l, i[j][1]

        if tx - fx == 0:
            for idy in range(min(fy, ty), max(fy, ty) + 1):
                state[idy][tx] = "#"
        elif ty - fy == 0:
            for idx in range(min(fx, tx), max(fx, tx) + 1):
                state[ty][idx] = "#"
        else:
            print("wtf, diagonal line???")

middle = int(500 - l)

done = False


def getstate(pos):

    if pos[0] >= 0 and pos[0] < len(
            state[0]) and pos[1] >= 0 and pos[1] < len(state):
        return state[pos[1]][pos[0]]
    else:
        global done
        done = True


counter = 0
while not done:
    curr = [middle, 0]
    rest = False
    while not rest:
        if getstate([curr[0], curr[1] + 1]) == " ":
            curr[1] += 1
        elif getstate([curr[0] - 1, curr[1] + 1]) == " ":
            curr[0] -= 1
        elif getstate([curr[0] + 1, curr[1] + 1]) == " ":
            curr[0] += 1
        else:
            if curr[1] >= 0 and curr[1] < len(state):
                state[curr[1]][curr[0]] = "O"
                rest = True
                counter += 1

#printstate()
print("Answer to part 1: ", counter - 1)

# PART 2
state = [[" " for _ in range(5000)] for _ in range(maxheight + 2)]
state.append(["#"] * len(state[0]))

l = 2000

for i in input:
    for j in range(1, len(i)):
        fx, fy = i[j - 1][0] + l, i[j - 1][1]
        tx, ty = i[j][0] + l, i[j][1]

        if tx - fx == 0:
            for idy in range(min(fy, ty), max(fy, ty) + 1):
                state[idy][tx] = "#"
        elif ty - fy == 0:
            for idx in range(min(fx, tx), max(fx, tx) + 1):
                state[ty][idx] = "#"

middle = int(500 + l)
done = False


def getstate2(pos):

    global done
    if pos[0] >= 0 and pos[0] < len(
            state[0]) and pos[1] >= 0 and pos[1] < len(state):
        return state[pos[1]][pos[0]]
    elif pos[1] >= len(state):
        print('POGGERS')
        done = True
    else:
        done = True


counter = 0
while not done:
    curr = [middle, 0]
    rest = False
    while not rest:
        if getstate2([curr[0], curr[1] + 1]) == " ":
            curr[1] += 1
        elif getstate2([curr[0] - 1, curr[1] + 1]) == " ":
            curr[0] -= 1
        elif getstate2([curr[0] + 1, curr[1] + 1]) == " ":
            curr[0] += 1
        else:
            if curr[1] >= 0 and curr[1] < len(state):
                state[curr[1]][curr[0]] = "O"
                rest = True
                counter += 1
    if state[0][middle] == "O":
        break

print("Answer to part 2: ", counter)
