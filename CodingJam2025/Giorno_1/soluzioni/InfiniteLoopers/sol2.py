with open("../../problema_2/input.txt", "r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

max_size = 0
max_row = 0
for idx, line in enumerate(lines):
    if line.startswith("$") or line.endswith("/"):
        continue
    size = int(line.split(" ")[0])
    if size > max_size:
        max_size = size
        max_row = idx

path = ""

for idx, line in enumerate(lines):
    if idx == max_row:
        path += line.split(" ")[1]
        break
    if line.startswith("$ cd"):
        dir = line.split(" ")[2]
        if dir == "..":
            path = path[: path[:-1].rindex("/") + 1]
        else:
            path += dir + "/"

print(path)
