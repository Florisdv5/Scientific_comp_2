import numpy as np
from C import find_candidates, select_value, calculate_SOR


def one_step(old_grid, omega, eta):
    new_grid = np.zeros(shape=(N, N))
    probs = np.zeros(N*N)
    probs_total = 0
    for y in range(len(old_grid)):
        for x in range(len(old_grid[0])):
            if old_grid[y][x] == 1:
                new_grid[y][x] = 1
            if find_candidates(old_grid, y, x) == True:
                prob = calculate_SOR(old_grid, new_grid, y, x, omega) ** eta
                probs[(y*N)+x] = prob
                probs_total += prob
    for x in range(len(probs)):
        probs[x] = probs[x] / probs_total
    i = select_value(probs)
    new_grid[i//N, i%N] = 1
    return new_grid

N = 20
matrix = np.zeros(shape=(N, N))
matrix[N - 1][np.random.randint(1, N - 1)] = 1
omega = 0.5
eta = 1
for step in range(100):
    matrix = one_step(matrix, omega, eta)
    print(matrix)