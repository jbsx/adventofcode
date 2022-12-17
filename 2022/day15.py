#!/usr/bin/python3
lines = [i.strip().split(": ") for i in open("inputday15", "r").readlines()]

answerrow = 2000000
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

ubound = 0
lbound = 0
for i in range(len(sensor)):
    sx, sy, bx, by = sensor[i][0], sensor[i][1], beacon[i][0], beacon[i][1]
    dist = abs(sx - bx) + abs(sy - by)
    cleared = dist - abs(sy - answerrow)
    ubound = max(ubound, sx + cleared + 1)
    lbound = min(lbound, sx, bx)

lbound = abs(lbound)
row = [0] * (ubound + lbound)

for i in range(len(sensor)):
    sx, sy, bx, by = sensor[i][0], sensor[i][1], beacon[i][0], beacon[i][1]
    dist = abs(sx - bx) + abs(sy - by)
    cleared = dist - abs(sy - answerrow)
    if cleared <= 0:
        continue

    f, t = sx - cleared, sx + cleared
    #print(f, t)
    #print(
    #    f"Source: ({sx}, {sy}) \nBeacon: ({bx}, {by})\ncleared = {cleared}\ndist = {dist}\n"
    #)
    for i in range(f, t + 1):
        if by == answerrow and bx == i:
            row[lbound + i] = -1
            continue
        row[lbound + i] += 1
#print(row)

res = 0
for i in row:
    if i > 0:
        res += 1
print("Answer to part 1: ", res)
#arr = open("inputday15", "r").readlines()
#sensors = []
#beacons = []
#for a in arr:
#    words = a.split(" ")
#    sensors.append(complex(int(words[2][2:-1]), int(words[3][2:-1])))
#    beacons.append(complex(int(words[8][2:-1]), int(words[9][2:])))
#y = 2000000
#empty_ranges = []
#for s, b in zip(sensors, beacons):
#    dist = abs(b.real - s.real) + abs(b.imag - s.imag)
#    max_x_dist = dist - abs(y - s.imag)
#    if max_x_dist >= 0:
#        empty_ranges.append([s.real - max_x_dist, s.real + max_x_dist + 1])
#
#unique_beacons = set(beacons)
#empty_ranges = sorted(empty_ranges)
#curr = empty_ranges[0]
#ans = 0
#i = 0
#while i < len(empty_ranges):
#    left, right = empty_ranges[i]
#    while i + 1 < len(empty_ranges) and empty_ranges[i + 1][0] <= right:
#        i += 1
#        right = max(right, empty_ranges[i][1])
#    else:
#        ans += right - left - len(
#            set([
#                b.real for b in unique_beacons
#                if b.imag == y and b.real >= left and b.imag < right
#            ]))
#        i += 1
#print(int(ans))
