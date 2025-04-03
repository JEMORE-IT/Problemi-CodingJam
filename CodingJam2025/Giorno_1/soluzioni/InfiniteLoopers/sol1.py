def chunkstring(string, length):
    return list(string[0 + i : length + i] for i in range(0, len(string), length))


with open("../../problema_1/input.txt", "r") as f:
    lines = f.readlines()

bad_bytes = ["11", "42", "00"]
good_bytes = ["13", "37", "2a", "b1"]

lines = [line.strip().split(" ") for line in lines[1:]]

for line in lines:
    ip = line[3][:-1]
    data = line[4]

    if len(data) / 2 != 32:
        continue
    if not data.startswith("4445445a") or not data.endswith("4e555453"):
        continue

    bytes = chunkstring(data, 2)
    bad = False
    for byte in bad_bytes:
        if byte in bytes:
            bad = True
            break
    if bad:
        continue

    good_counter = 0
    for byte in good_bytes:
        if byte in bytes:
            good_counter += 1
    if good_counter >= 3:
        break

print(ip)
