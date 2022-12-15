#!/usr/bin/python3
from functools import reduce
from math import lcm

file = open("inputday11", "r")
lines = file.readlines()


class Monkey:

    def __init__(self):
        self.items = []
        self.op = lambda a: a
        self.test = 1
        self.test1 = 2
        self.test2 = 3
        self.total = 0

    def inspect(self):
        for n in range(len(self.items)):

            self.items[n] = self.op(self.items[n])

            #Monkey gets bored
            self.items[n] = self.items[n] // 3

            #Throw item
            if self.items[n] % self.test == 0:
                monkeys[self.test1].items.append(self.items[n])
            else:
                monkeys[self.test2].items.append(self.items[n])
        self.total += len(self.items)
        self.items.clear()

    def inspect2(self):
        for n in range(len(self.items)):

            self.items[n] = self.op(self.items[n])

            #Modulo
            modulus = reduce(lcm, [m.test for m in monkeys])
            item = self.items[n] % modulus

            #Throw item
            if self.items[n] % self.test == 0:
                monkeys[self.test1].items.append(item)
            else:
                monkeys[self.test2].items.append(item)
        self.total += len(self.items)
        self.items.clear()


# Parse Input
def parse():
    monkeys = []
    for i in lines:
        commands = i.strip().split()

        if len(commands) == 0:
            continue

        if commands[0] == "Monkey":
            monkeys.append(Monkey())
        elif commands[0] == "Starting":
            for j in range(2, len(commands)):
                monkeys[-1].items.append(int(commands[j].split(",")[0]))
        elif commands[0] == "Operation:":
            op = " ".join([commands[-3], commands[-2], commands[-1]])
            monkeys[-1].op = eval(f"lambda old: {op}")
        elif commands[0] == "Test:":
            monkeys[-1].test = int(commands[3])
        elif commands[1] == "true:":
            monkeys[-1].test1 = int(commands[5])
        elif commands[1] == "false:":
            monkeys[-1].test2 = int(commands[5])
    return monkeys


# PART 1

monkeys = parse()
for _ in range(20):
    for i in monkeys:
        i.inspect()

inspections = sorted([m.total for m in monkeys])
print("Answer to part 1: ", inspections[-1] * inspections[-2])

# PART 2

monkeys = parse()
for j in range(10000):
    for i in monkeys:
        i.inspect2()

inspections = sorted([m.total for m in monkeys])
print("Answer to part 2: ", inspections[-1] * inspections[-2])
