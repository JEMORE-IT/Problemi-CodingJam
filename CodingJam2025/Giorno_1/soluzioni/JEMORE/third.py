import sys

sys.setrecursionlimit(2147483647)

p_cache = {}
j_cache = {}

def padovan(n):
    if n <= 2:
        return 1
    if n not in p_cache:
        p_cache[n] = padovan(n-2) + padovan(n-3)
    return p_cache[n]

def jacob(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    p1 = padovan(n - 1)
    p2 = padovan(n - 2)

    if p1 >= n or p2 >= n:
        n1 = n - 1
        n2 = n - 2
    else:
        n1 = n - p1
        n2 = n - p2
    
    if n1 not in j_cache:
        j_cache[n1] = jacob(n1)
    if n2 not in j_cache:
        j_cache[n2] = jacob(n2)
        
    
    return j_cache[n1] + 2 * j_cache[n2]

n = 2025
print(jacob(n) % 1000000)
