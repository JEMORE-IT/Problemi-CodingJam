import functools


@functools.cache
def p(n):
    if n == 0 or n == 1 or n == 2:
        return 1

    el = p(n - 2) + p(n - 3)
    return el


@functools.cache
def j(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    if (p(n - 1) >= n) or (p(n - 2) >= n):
        el = j(n - 1) + 2 * j(n - 2)

        return el

    el = j(n - p(n - 1)) + 2 * j(n - p(n - 2))

    return el


if __name__ == "__main__":
    for i in range(0, 2026):
        j(i)
    print(j(2025) % 10**6)
