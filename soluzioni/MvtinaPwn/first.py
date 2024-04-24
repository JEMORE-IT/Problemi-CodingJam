OPEN = ["(", "{", "[", "<"]

close_of = {
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">"
}

points = {
    ")": 7,
    "]": 42,
    "}": 1337,
    ">": 64880
}

ans = 0
def check(line):
    stack = []
    for c in line:
        if c in OPEN:
            stack.append(close_of[c])
        else:
            if c != stack.pop():
                return c
    return None


with open("debug_primo.txt") as f:
    for line in f:
        line = line.strip()
        print("Line: ", line)
        c = check(line)
        if c != None:
            print("C: ", c)
            ans += points[c]

print(ans)