#!/usr/bin/python3
file = open("inputday9", "r")
lines = file.readlines()

map = {
    "L": [-1, 0],
    "U": [0, 1],
    "R": [1, 0],
    "D": [0, -1],
}

head = [0, 0]
tail = [0, 0]

visited = set()


def move(d):
    head[0] += d[0]
    head[1] += d[1]

    xdiff = head[0] - tail[0]
    ydiff = head[1] - tail[1]

    #1st quadrant
    if (xdiff > 1 and ydiff >= 1) or (xdiff >= 1 and ydiff > 1):
        tail[0] += 1
        tail[1] += 1
    #2nd quadrant
    elif (xdiff < -1 and ydiff >= 1) or (xdiff <= -1 and ydiff > 1):
        tail[0] -= 1
        tail[1] += 1
    #3nd quadrant
    elif (xdiff < -1 and ydiff <= -1) or (xdiff <= -1 and ydiff < -1):
        tail[0] -= 1
        tail[1] -= 1
    #4nd quadrant
    elif (xdiff > 1 and ydiff <= -1) or (xdiff >= 1 and ydiff < -1):
        tail[0] += 1
        tail[1] -= 1

    # Horizontal
    elif xdiff < -1:
        tail[0] -= 1
    elif xdiff > 1:
        tail[0] += 1
    # Vertical
    elif ydiff < -1:
        tail[1] -= 1
    elif ydiff > 1:
        tail[1] += 1

    visited.add(tuple(tail))


for line in lines:
    commands = line.strip().split()
    for _ in range(int(commands[1])):
        move(map.get(commands[0]))

print("Answer to part 1: ", len(visited))

#PART 2

head = [0, 0]
tail = [0, 0]

knots = [[0, 0] for _ in range(10)]

visited = set()


def move2(d):
    for (i, curr) in enumerate(knots):
        if i == 0:
            knots[i][0] += d[0]
            knots[i][1] += d[1]
            continue

        head = knots[i - 1]
        tail = curr

        xdiff = head[0] - tail[0]
        ydiff = head[1] - tail[1]

        #1st quadrant
        if (xdiff > 1 and ydiff >= 1) or (xdiff >= 1 and ydiff > 1):
            tail[0] += 1
            tail[1] += 1
        #2nd quadrant
        elif (xdiff < -1 and ydiff >= 1) or (xdiff <= -1 and ydiff > 1):
            tail[0] -= 1
            tail[1] += 1
        #3nd quadrant
        elif (xdiff < -1 and ydiff <= -1) or (xdiff <= -1 and ydiff < -1):
            tail[0] -= 1
            tail[1] -= 1
        #4nd quadrant
        elif (xdiff > 1 and ydiff <= -1) or (xdiff >= 1 and ydiff < -1):
            tail[0] += 1
            tail[1] -= 1

        # Horizontal
        elif xdiff < -1:
            tail[0] -= 1
        elif xdiff > 1:
            tail[0] += 1
        # Vertical
        elif ydiff < -1:
            tail[1] -= 1
        elif ydiff > 1:
            tail[1] += 1

    visited.add(tuple(knots[-1]))


for line in lines:
    commands = line.strip().split()
    for _ in range(int(commands[1])):
        move2(map.get(commands[0]))

print("Answer to part 2: ", len(visited))
