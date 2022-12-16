#!/usr/bin/python3
lines = [i.strip().split(": ") for i in open("inputday15", "r").readlines()]

answerrow = 10
sensor = []
beacon = []
for i in lines:
    #sensor
    j = i[0].split("at ")[1]
    x = int(j.split(", ")[0].split("=")[1])
    y = int(j.split(", ")[1].split("=")[1])
    sensor.append([x, y])

    #beacon
    j = i[1].split("at ")[1]
    x = int(j.split(", ")[0].split("=")[1])
    y = int(j.split(", ")[1].split("=")[1])
    beacon.append([x, y])

length = 0
for i in range(len(sensor)):
    sx, sy, bx, by = sensor[i][0], sensor[i][1], beacon[i][0], beacon[i][1]
    dist = (sx - bx) + (sy - by)
    length = max(length, sx + (dist - abs(sy - answerrow)))

row = [0] * length
for i in range(len(sensor)):
    sx, sy, bx, by = sensor[i][0], sensor[i][1], beacon[i][0], beacon[i][1]
    dist = (sx - bx) + (sy - by)
    cleared = dist - abs(sy - answerrow)
    print(cleared)
    f, t = sx - cleared // 2, sx + cleared // 2

res = 0
for i in row:
    if i == 1:
        res += 1
print("Answer to part 1: ", row)
