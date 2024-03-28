from collections import deque

with open("input_1.txt") as f:
    lines = [l.strip() for l in f.readlines()]

mapping = { "}": ["{", 1337], "]" : ["[", 42], ")" : ["(", 7], ">" : ["<", 64880] }

points = 0
for line in lines:
    stack = deque()
    for c in line:
        if c in "{([<":
            stack.append(c)
        else:
            if stack.pop() != mapping[c][0]:
                points += mapping[c][1]
                continue

print(points)
