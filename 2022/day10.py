#!/usr/bin/python3
file = open("inputday10", "r")
lines = file.readlines()

bruh = [20, 60, 100, 140, 180, 220]

# PART 1

clock = 0
x = 1
res = 0
seen = False
c = 0

while c < len(lines):
    commands = lines[c].strip().split()

    clock += 1

    if clock in bruh:
        res += (clock * x)

    if commands[0] == "addx":
        if seen:
            x += int(commands[1])
            c += 1
        seen = not seen
    elif commands[0] == "noop":
        c += 1

print("Answer to part 1: ", res)

#PART 2

crt = []
clock = 0
res = "\n"
x = 1
seen = False
c = 0

while c < len(lines):
    commands = lines[c].strip().split()

    # Increment clock
    clock += 1

    # PRINT
    sprite = [x - 1, x, x + 1]
    drawing = (clock - 1) % 40
    if drawing in sprite:
        res += "█"
    else:
        res += " "

    if drawing == 39:
        res += "\n"

    # Compute
    if commands[0] == "addx":
        if seen:
            x += int(commands[1])
            c += 1
        seen = not seen
    elif commands[0] == "noop":
        c += 1

print("Answer to part 2: ", res)
