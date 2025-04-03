import numpy as np
import heapq


def isValidCell(i, j, n, m):
    return 0 <= i < n and 0 <= j < m


def minimumCostPath(cost_matrix, start, end, grid):
    n, m = len(cost_matrix), len(cost_matrix[0])

    pq = []

    cost = [[float("inf")] * m for _ in range(n)]

    paths = {}

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    x, y = start
    heapq.heappush(pq, (cost_matrix[x][y], x, y))
    cost[x][y] = cost_matrix[x][y]
    paths[(x, y)] = grid[x][y]

    while pq:
        c, i, j = heapq.heappop(pq)

        if (i, j) == end:
            return paths[(i, j)], cost[i][j]

        for dx, dy in directions:
            ni, nj = i + dx, j + dy

            if isValidCell(ni, nj, n, m):
                new_cost = c + cost_matrix[ni][nj]

                if new_cost < cost[ni][nj]:
                    cost[ni][nj] = new_cost
                    heapq.heappush(pq, (new_cost, ni, nj))
                    paths[(ni, nj)] = paths[(i, j)] + grid[ni][nj]

    return None, float("inf")


with open("../../problema_4/matrix.txt", "r") as f:
    matrix = f.readlines()

matrix = [list(line.strip()) for line in matrix]
M = len(matrix)
N = len(matrix[0])

starting_points = []
ending_points = []

values = np.zeros((M, N))
for r in range(M):
    for c in range(N):
        char = matrix[r][c]
        if char.isalpha():
            if char.islower():
                if char == "a":
                    starting_points.append((r, c))
                elif char == "z":
                    ending_points.append((r, c))
                values[r][c] = ord(char) % 10
            else:
                values[r][c] = ord(char.lower()) % 10
        elif char.isnumeric():
            values[r][c] = float(char)
        else:
            values[r][c] = float("inf")

best_path = ""
best_cost = float("inf")

for start in starting_points:
    for end in ending_points:
        curr_path, curr_cost = minimumCostPath(values, start, end, matrix)
        if curr_cost < best_cost:
            best_path = curr_path
            best_cost = curr_cost
            print(best_cost, best_path)
            print()

# SOLUTION: agOS4Pwhq2chhXHy54l1FdxRugnr4nXk3dxUqOniU0Pdg5OxgxsoxNCnbnYX0ynTweHt0PHQKNJ0yy79k62oNxQnFl3j5qrpNG3z (cost: 302)
