lines = []
with open("input.txt") as f:
    lines = f.readlines()

matrix = [l.replace('\n', '').split(" ") for l in lines]
side = len(matrix[0])
steps = 200
sx, sy = 6, 3
dir = (-1, 0)

random_chars = ["O", "p", "T", "0", "<", ">"]
value_map = {
    "O": 210,
    "p": 136,
    "T": 60,
    "0": 421,
    "<": 130,
    ">": 370
}

def calculate_score():
    score = 0
    for row_idx in range(side):
        for col_idx in range(side):
            c = matrix[row_idx][col_idx]
            if c in value_map.keys():
                score += value_map[c] * row_idx + col_idx
    return score

print(f"Starting from {sx},{sy}")
print(f"Starting dir {dir}")

def print_matrix():
    copy = [l.copy() for l in matrix]
    print(f"Current position: {sx},{sy}")
    copy[sy][sx] = "*"

    print(f"Score: {calculate_score()}")
    print("\n".join(" ".join(l) for l in copy))

print_matrix()

def apply_right(dx, dy):
    if dx == -1 and dy == 0:
        return 0, -1
    elif dx == 0 and dy == -1:
        return 1, 0
    elif dx == 1 and dy == 0:
        return 0, 1
    else:
        return -1, 0

def apply_left(dx, dy):
    if dx == -1 and dy == 0:
        return 0, 1
    elif dx == 0 and dy == 1:
        return 1, 0
    elif dx == 1 and dy == 0:
        return 0, -1
    else:
        return -1, 0

movement_map = {
    "o": lambda dx, dy: apply_right(dx, dy),
    "-": lambda dx, dy: apply_left(dx, dy),
}

prev_char = None
for i in range(steps):
    wall = matrix[(sy + dir[1]) % side][(sx + dir[0]) % side]
    if wall in movement_map:
        prev_char = wall
        dir = movement_map[prev_char](dir[0], dir[1])

    sx = (sx + int(dir[0])) % side
    sy = (sy + int(dir[1])) % side

    next_char = matrix[sy][sx]
    if next_char in random_chars:
        matrix[sy][sx] = random_chars[(random_chars.index(next_char) + 1) % len(random_chars)]
    
    # Uncomment these lines to view how the matrix
    # changes step by step
    #print_matrix()
    #input("")
print_matrix()
print(calculate_score())
