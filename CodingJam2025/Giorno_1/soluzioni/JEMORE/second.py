lines: list[str] = []
with open("input.txt", "r") as file:
    lines = [s.strip() for s in file.readlines()]

wd = ""
bestName = None
bestSize = 0
for command in lines:
    if command.startswith("$"):
        if "cd" in command:
            target = command[5:]
            if target == "..":
                wd = wd[:wd.rfind("/")]
            else:
                wd = f"{wd}/{target}"
    else:
        size, name = command.split(" ")
        if not name.endswith("/") and int(size) > bestSize:
            bestSize = int(size)
            bestName = f"{wd}/{name}"

print(f"{bestName} @ {bestSize}")
