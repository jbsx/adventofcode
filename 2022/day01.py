#!/usr/bin/python3
file = open("inputday1", "r")
lines = file.readlines()
output = [0]

for i in lines:
    if i == '\n':
        output.append(0)
    else:
        output[-1] += int(i)

# Part 1
res = 0
for i in output:
    res = max(res, i)
print("Answer to part 1:", res)

# Part 2
temp = [output[0], output[1], output[2]]
for i in output:
    if i > temp[0]:
        temp = [i, temp[0], temp[1]]
    elif i > temp[1]:
        temp = [temp[0], i, temp[1]]
    elif i > temp[2]:
        temp = [temp[0], temp[1], i]
res = 0
for i in temp:
    res += i
print("Answer to part 2:", res)
