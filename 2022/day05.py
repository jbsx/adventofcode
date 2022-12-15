#!/usr/bin/python3
file = open("inputday5", "r")
lines = file.readlines()

stacks = int(len(lines[0]) / 4)

# PART 1
state = [[] for _ in range(stacks)]
divline = 0
for (i, line) in enumerate(lines):
    if len(line.strip()) == 0:
        divline = i - 1
        break

for i in range(divline - 1, -1, -1):
    for j in range(stacks):
        index = 1 + (j * 4)
        if lines[i][index] != ' ':
            state[j].append(lines[i][index])

for i in range(divline + 2, len(lines)):
    values = lines[i].split()
    amount = int(values[1])
    fromstack = int(values[3])
    tostack = int(values[5])

    temp = []
    for _ in range(amount):
        temp.append(state[fromstack - 1].pop())
    state[tostack - 1] += temp
    #for _ in range(amount):
    #    state[tostack - 1].append(temp.pop())
res = ""
for i in state:
    res += i.pop()

print("Answer for part 1: ", res)

# PART 2
state = [[] for _ in range(stacks)]
divline = 0
for (i, line) in enumerate(lines):
    if len(line.strip()) == 0:
        divline = i - 1
        break

for i in range(divline - 1, -1, -1):
    for j in range(stacks):
        index = 1 + (j * 4)
        if lines[i][index] != ' ':
            state[j].append(lines[i][index])
for i in range(divline + 2, len(lines)):
    values = lines[i].split()
    amount = int(values[1])
    fromstack = int(values[3])
    tostack = int(values[5])

    temp = []
    for _ in range(amount):
        temp.append(state[fromstack - 1].pop())
    for _ in range(amount):
        state[tostack - 1].append(temp.pop())
res = ""
for i in state:
    res += i.pop()
print("Answer for part 2: ", res)
