#!/usr/bin/python3
file = open("inputday6", "r")
input = file.readlines()[0].strip()

# PART 1
res = 0
for i in range(3, len(input)):
    if len(set(input[(i - 4):i])) == 4:
        res = i
        break

print("Answer for Part 1: ", res)

# PART 2
start = res
res = 0
for i in range(13, len(input)):
    if len(set(input[(i - 14):i])) == 14:
        res = i
        break

print("Answer for Part 2: ", res)
