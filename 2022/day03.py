#!/usr/bin/python3
file = open("inputday3", "r")
lines = file.readlines()

shared = ""
for items in lines:
    seen = set()
    for i in range(int(len(items.strip()) / 2)):
        seen.add(items[i])
    for i in range(int(len(items.strip()) / 2), len(items.strip())):
        if items[i] in seen:
            shared += items[i]
            break

res = 0
for i in shared:
    if i.islower():
        res += ord(i) - 96
    else:
        res += ord(i) - 64 + 26
print("Answer to part 1: ", res)

shared = ""
seen = set()
candidates = set()
offset = -1
for items in lines:
    offset += 1
    if offset == 0:
        seen = set(items)
    elif offset == 1:
        for i in items:
            if i in seen:
                candidates.add(i)
    else:
        for i in items:
            if i in candidates:
                shared += i

                offset = -1
                seen.clear()
                candidates.clear()
                break

res = 0
for i in shared:
    if i.islower():
        res += ord(i) - 96
    else:
        res += ord(i) - 64 + 26
print("Answer to part 2: ", res)
