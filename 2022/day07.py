#!/usr/bin/python3
from collections import defaultdict

file = open("inputday7", "r")
lines = file.readlines()

size = defaultdict(list)
currdir = []

for i in lines:
    values = i.split()

    if values[0] == '$' and values[1] == 'cd':
        if values[2] == '..':
            currdir.pop()
        else:
            currdir.append(values[2])
    elif values[0].isdigit():
        size["/".join(currdir)].append(values[0])
    elif values[0] == 'dir':
        size["/".join(currdir)].append(values[1])

memoizeD = {}


def flatmap(index):
    if index in memoizeD:
        return memoizeD[index]

    for i in size[index]:
        if i.isdigit():
            memoizeD[index] = memoizeD.get(index, 0) + int(i)
        else:
            memoizeD[index] = memoizeD.get(index, 0) + flatmap(index + '/' + i)
    return memoizeD[index]


flatmap('/')
res = 0
for i in memoizeD.values():
    if i < 100000:
        res += i
print("Answer for part 1: ", res)

unused = 70000000 - memoizeD['/']
target = 30000000 - unused
res = float('inf')
for i in memoizeD.values():
    if i > target:
        res = min(res, i)
print("Answer for part 2: ", res)
