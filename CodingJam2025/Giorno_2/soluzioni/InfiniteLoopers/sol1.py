def chunkstring(string, length):
    return list(string[0 + i : length + i] for i in range(0, len(string), length))


with open("../../problema_1/matrix.txt", "r") as f:
    lines = f.readlines()

lines = [line.strip().split(" ") for line in lines]

bits = ""

for a, b in lines:
    start_idx = 0
    while a.startswith(b[: start_idx + 1]):
        start_idx += 1
    start = b[:start_idx]
    end_idx = len(b)
    while a.endswith(b[end_idx - 1 :]) and end_idx > start_idx:
        end_idx -= 1
    end = b[end_idx:]
    if start + end == b:
        bits += "1"
    else:
        bits += "0"

for byte in chunkstring(bits, 8):
    print(chr(int(byte, 2)), end="")
print()
