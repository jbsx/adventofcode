#!/usr/bin/python3
def bruh(i):
    return i.strip()


lines = list(map(bruh, open("inputday8", "r").readlines()))

# PART 1
visible = 0

for (line_y, line) in enumerate(lines):
    for (line_x, value) in enumerate(line):

        isvis = [True for _ in range(4)]

        #check left
        for i in range(line_x - 1, -1, -1):
            if int(lines[line_y][i]) >= int(value):
                isvis[0] = False
                break

        #check up
        for i in range(line_y - 1, -1, -1):
            if int(lines[i][line_x]) >= int(value):
                isvis[1] = False
                break

        #check right
        for i in range(line_x + 1, len(line)):
            if int(lines[line_y][i]) >= int(value):
                isvis[2] = False
                break

        #check down
        for i in range(line_y + 1, len(lines)):
            if int(lines[i][line_x]) >= int(value):
                isvis[3] = False
                break

        #if visible from any edge
        if True in isvis:
            visible += 1

print("Answer to part 1: ", visible)

# PART 2
res = 0
for (line_y, line) in enumerate(lines):
    for (line_x, value) in enumerate(line):
        scenicscore = 1

        if line_y == 0 or line_y == len(
                lines) - 1 or line_x == 0 or line_x == len(line) - 1:
            continue

        #check left
        for i in range(line_x - 1, -1, -1):
            if int(lines[line_y][i]) >= int(value) or i == 0:
                scenicscore *= (line_x - i)
                break

        #check up
        for i in range(line_y - 1, -1, -1):
            if int(lines[i][line_x]) >= int(value) or i == 0:
                scenicscore *= (line_y - i)
                break

        #check right
        for i in range(line_x + 1, len(line)):
            if int(lines[line_y][i]) >= int(value) or i == len(line) - 1:
                scenicscore *= (i - line_x)
                break

        #check down
        for i in range(line_y + 1, len(lines)):
            if int(lines[i][line_x]) >= int(value) or i == len(lines) - 1:
                scenicscore *= (i - line_y)
                break

        if scenicscore >= res:
            res = max(res, scenicscore)

print("Answer to part 2: ", res)
