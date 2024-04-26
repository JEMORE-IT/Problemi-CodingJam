with open("test.txt", "r") as f:
    acc = 0
    for line in f:
        line = line.strip()
        n, k = line.split(" ")
        n = int(n)
        k = int(k)

        if (k + 1) % (2 ** n) == 0:
            acc = acc + 1

print(acc)