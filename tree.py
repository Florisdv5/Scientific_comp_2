import numpy as np
from SOR_funcs import find_candidates, select_value, calculate_SOR
import matplotlib.pyplot as plt
from tqdm import tqdm


def one_step(old_grid, omega, eta):
    probs = np.zeros(N*N) # List of 10000 zero's
    probs_total = 0
    new_grid = old_grid[:]
    for y in range(len(old_grid)):
        for x in range(len(old_grid[0])):
            if find_candidates(old_grid, y, x) == True:
                prob = calculate_SOR(old_grid, new_grid, y, x, omega) ** eta
                probs[(y*N)+x] = prob
                probs_total += prob
    for x in range(len(probs)):
        probs[x] = probs[x] / probs_total
    i = select_value(probs)
    new_grid[i//N, i%N] = 1
    return new_grid


N = 100
matrix_structure = np.zeros(shape=(N, N))
matrix_concentration = np.zeros(shape=(N, N))
matrix_structure[0][int(N/2)] = 1
omega = 1.8
eta = 3
# matrix = one_step(matrix, omega, eta)
for step in tqdm(range(600)):
    matrix = one_step(matrix_structure, omega, eta)

y_values = np.linspace(0, 1, num=N+1)
plt.pcolormesh(y_values, y_values, matrix_structure)
plt.show()