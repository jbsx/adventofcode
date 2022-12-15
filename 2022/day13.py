#!/usr/bin/python3
#Parse
lines = [i.strip() for i in open("inputday13", "r").readlines()]
input = []
temp = []
for i in lines:
    if len(i) == 0:
        input.append(temp[:])
        temp.clear()
        continue
    temp.append(i)

# PART 1


def compare(left, right):
    if type(left) != type(right):
        if type(left) == list:
            return compare(left, [right])
        else:
            return compare([left], right)
    elif type(left) == int and type(right) == int:
        if left < right:
            return True
        elif right < left:
            return False
        else:
            return -1
    elif type(left) == list and type(right) == list:
        for i in range(max(len(left), len(right))):
            if i >= len(right) and not i >= len(left):
                return False
            if i >= len(left) and not i >= len(right):
                return True

            temp = compare(left[i], right[i])
            if temp == -1:
                continue
            else:
                return temp
    return -1


res = 0
for (idx, bruh) in enumerate(input):
    left = eval(bruh[0])
    right = eval(bruh[1])

    if compare(left, right):
        res += idx + 1
print("Answer to part 1: ", res)

#PART 2

input2 = [[[2]], [[6]]]
for i in lines:
    if i != "":
        input2.append(eval(i))

sorted = False

while not sorted:
    temp = False
    for i in range(1, len(input2)):
        if not compare(input2[i - 1], input2[i]):
            input2[i - 1], input2[i] = input2[i], input2[i - 1]
            temp = True
    if not temp:
        sorted = True

print("Answer to part 2: ",
      (input2.index([[2]]) + 1) * (input2.index([[6]]) + 1))
