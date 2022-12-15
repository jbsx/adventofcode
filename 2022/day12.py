#!/usr/bin/python3
from collections import deque

grid = [list(i.strip()) for i in open("inputday12", "r").readlines()]
dir = [
    [-1, 0],  #LEFT
    [0, -1],  #UP
    [1, 0],  #RIGHT
    [0, 1],  #DOWN
]

start = []
end = []
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "S":
            grid[y][x] = 'a'
            start = [x, y, 0]
        if grid[y][x] == 'E':
            grid[y][x] = 'z'
            end = [x, y, float('inf')]

q = deque()
q.append(start)
visited = [[start[0], start[1]]]
answers = []

while len(q) > 0:
    curr = q.popleft()

    for i in dir:
        nx = curr[0] + i[0]
        ny = curr[1] + i[1]

        if nx < 0 or nx >= len(grid[0]) or ny < 0 or ny >= len(grid):
            continue

        diff = ord(grid[ny][nx]) - ord(grid[curr[1]][curr[0]])
        if diff > 1:
            continue

        if [nx, ny] in visited:
            continue
        if nx == end[0] and ny == end[1]:
            answers.append(curr[-1] + 1)
            break

        visited.append([nx, ny])
        q.append([nx, ny, curr[-1] + 1])
sorted(answers)
print("Answer to part 1", answers[0])

# PART 2
start, end = end, start
end[-1] = start[-1]
start[-1] = 0

q = deque()
q.append(start)
visited = [start]
answers = []

while len(q) > 0:
    curr = q.popleft()

    for i in dir:
        nx = curr[0] + i[0]
        ny = curr[1] + i[1]

        if nx < 0 or nx >= len(grid[0]) or ny < 0 or ny >= len(grid):
            continue

        diff = ord(grid[ny][nx]) - ord(grid[curr[1]][curr[0]])
        if diff < -1:
            continue

        if [nx, ny] in visited:
            continue
        if grid[ny][nx] == "a":
            answers.append(curr[-1] + 1)
            break

        visited.append([nx, ny])
        q.append([nx, ny, curr[-1] + 1])

sorted(answers)
print("Answer to part 2", answers[0])
