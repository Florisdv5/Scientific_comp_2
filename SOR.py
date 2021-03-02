import numpy as np
from SOR_funcs import find_candidates, select_value, calculate_SOR
import matplotlib.pyplot as plt

def one_step(old_old_grid, old_grid, omega, eta):
    probs = np.zeros(N*N)
    probs_total = 0
    new_grid = np.zeros(shape=(N, N))
    for y in range(len(old_grid)):
        for x in range(len(old_grid[0])):
            if old_grid[y][x] == 1:
                new_grid[y][x] = 1
            if find_candidates(old_grid, y, x) == True:
                prob = calculate_SOR(old_old_grid, old_grid, y, x, omega) ** eta
                probs[(y*N)+x] = prob
                probs_total += prob
    for x in range(len(probs)):
        probs[x] = probs[x] / probs_total
    #print(probs)
    i = select_value(probs)
    new_grid[i//N][i%N] = 1
    return new_grid, old_grid

N = 100
matrix = np.zeros(shape=(N, N))
old_matrix = matrix.copy()
matrix[N - 1][np.random.randint(1, N - 1)] = 1
omega = 1.8
eta = 2
for step in range(600):
    matrix, old_matrix = one_step(old_matrix, matrix, omega, eta)
    #plt.show()
plt.matshow(matrix)
plt.show()