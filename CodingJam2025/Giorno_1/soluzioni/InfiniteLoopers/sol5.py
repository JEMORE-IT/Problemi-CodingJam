STEPS = 200
SIZE = 32
SYMBOLS = {"O": 210, "p": 136, "T": 60, "0": 421, "<": 130, ">": 370}
DIRS = [(0, -1), (-1, 0), (0, 1), (1, 0)]


def step(pos: tuple, dir: tuple):
    next_pos = [pos[0] + dir[0], pos[1] + dir[1]]

    if next_pos[0] == -1:
        next_pos[0] = SIZE - 1
    elif next_pos[0] == SIZE:
        next_pos[0] = 0

    if next_pos[1] == -1:
        next_pos[1] = SIZE - 1
    elif next_pos[1] == SIZE:
        next_pos[1] = 0

    return tuple(next_pos)


with open("../../problema_5/input.txt", "r") as f:
    lines = f.readlines()

lines = [line.strip().split(" ") for line in lines]
robot_pos = (3, 6)
dir_idx = 0

for _ in range(STEPS):
    next_pos = step(robot_pos, DIRS[dir_idx])
    if lines[next_pos[0]][next_pos[1]] == "o":
        if dir_idx == 3:
            dir_idx = 0
        else:
            dir_idx += 1
    elif lines[next_pos[0]][next_pos[1]] == "-":
        if dir_idx == 0:
            dir_idx = 3
        else:
            dir_idx -= 1
    robot_pos = step(robot_pos, DIRS[dir_idx])
    symbol = lines[robot_pos[0]][robot_pos[1]]
    if symbol in SYMBOLS:
        symbol_idx = list(SYMBOLS).index(symbol)
        if symbol_idx == len(SYMBOLS) - 1:
            symbol_idx = 0
        else:
            symbol_idx += 1
        lines[robot_pos[0]][robot_pos[1]] = list(SYMBOLS)[symbol_idx]


res = 0
for r in range(SIZE):
    for c in range(SIZE):
        if lines[r][c] in SYMBOLS:
            res += r * SYMBOLS[lines[r][c]] + c

print(res)
