#!/usr/bin/python3
file = open("inputday2", "r")
lines = file.readlines()

mapping = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}

res = 0
for i in lines:
    if mapping[i[2]] == "rock":
        res += 1
        if mapping[i[0]] == "rock":
            res += 3
        elif mapping[i[0]] == "paper":
            res += 0
        else:
            res += 6
    elif mapping[i[2]] == "paper":
        res += 2
        if mapping[i[0]] == "rock":
            res += 6
        elif mapping[i[0]] == "paper":
            res += 3
        else:
            res += 0
    elif mapping[i[2]] == "scissors":
        res += 3
        if mapping[i[0]] == "rock":
            res += 0
        elif mapping[i[0]] == "paper":
            res += 6
        else:
            res += 3
print("Answer for part 1: ", res)

res = 0
for i in lines:
    if i[2] == "X":
        res += 0
        if mapping[i[0]] == "rock":
            res += 3
        elif mapping[i[0]] == "paper":
            res += 1
        else:
            res += 2
    elif i[2] == "Y":
        res += 3
        if mapping[i[0]] == "rock":
            res += 1
        elif mapping[i[0]] == "paper":
            res += 2
        else:
            res += 3
    else:
        res += 6
        if mapping[i[0]] == "rock":
            res += 2
        elif mapping[i[0]] == "paper":
            res += 3
        else:
            res += 1
print("Answer for part 2: ", res)
