#!/usr/bin/python3
lines = [i.strip().split(": ") for i in open("inputday15", "r").readlines()]

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
