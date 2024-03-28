with open("input_2.txt") as f:
    lines = [l.split() for l in f.readlines()]
    lines = [[int(n), int(k)] for n, k in lines]

total = 0
for n, k in lines:
      p = pow(2, n)
      if k % p == p - 1:
           total += 1

print(total)