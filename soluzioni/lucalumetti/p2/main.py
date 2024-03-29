import sys
data = sys.stdin.read().splitlines()
total = 0
for line in data:
    N, K = [int(x) for x in line.split(' ')]
    two_n = pow(2, N)
    total += N == 0 or (two_n-1 == K % two_n)
print(total)
