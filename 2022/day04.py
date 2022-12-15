#!/usr/bin/python3
file = open("inputday4", "r")
lines = file.readlines()

#PART 1
res = 0
for line in lines:
    #parse
    temp = line.strip().split(",")
    range1 = temp[0].split("-")
    range2 = temp[1].split("-")

    #check ranges
    if int(range1[0]) <= int(range2[0]) and int(range1[1]) >= int(range2[1]):
        res += 1
    elif int(range2[0]) <= int(range1[0]) and int(range2[1]) >= int(range1[1]):
        res += 1

print("Answer for part 1: ", res)

#PART 2
res = 0
for line in lines:
    #parse
    temp = line.strip().split(",")
    range1 = temp[0].split("-")
    range2 = temp[1].split("-")

    #check ranges
    if int(range2[0]) <= int(range1[1]) and int(range2[1]) >= int(range1[0]):
        res += 1
    elif int(range1[0]) <= int(range2[1]) and int(range1[1]) >= int(range2[0]):
        res += 1

print("Answer for part 2: ", res)
