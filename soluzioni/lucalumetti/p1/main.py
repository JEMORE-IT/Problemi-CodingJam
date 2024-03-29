import sys
data = sys.stdin.read().splitlines()

op = '(<[{'
cl = ')>]}'

points = {
    ')': 7,
    ']': 42,
    '}': 1337,
    '>': 64880
}

total = 0
for line in data:
    stack = []
    for ch in line:
        if ch in op:
            stack.append(ch)
            continue
        if op.index(stack.pop()) == cl.index(ch):
            continue
        total += points[ch]
print(total)
