import numpy as np
from SOR_funcs import update_SOR, initialise_grid, find_neighbours, concentration_neighbours
import matplotlib.pyplot as plt
from tqdm import tqdm
from DLA_constants import n_size, steps, eta


def one_step(matrix_structure, matrix_concentration):
    matrix_concentration = update_SOR(matrix_structure, matrix_concentration)
    neighbours = find_neighbours(matrix_structure)
    neighbours_conc = concentration_neighbours(neighbours, matrix_concentration)

    sum_candidates_conc = 0
    for i in range(len(neighbours_conc)):
        sum_candidates_conc += neighbours_conc[i] ** eta
    probabilities = []
    for i in range(len(neighbours_conc)):
        probabilities.append(neighbours_conc[i] ** eta / sum_candidates)

    choice = np.random.choice(len(neighbours), p=probabilities)
    added_neighbour = neighbours[choice]
    matrix_structure[added_neighbour[0]][added_neighbour[1]] = 1
    return matrix_structure, matrix_concentration


y_values = np.linspace(0, 1, num=n_size + 1)
matrix_structure = np.zeros(shape=(n_size, n_size))
matrix_structure[0][int(n_size / 2)] = 1
matrix_concentration = initialise_grid()

for step in tqdm(range(steps)):
    matrix_structure, matrix_concentration = one_step(matrix_structure, matrix_concentration)

y_values = np.linspace(0, 1, num=n_size + 1)
plt.pcolormesh(y_values, y_values, matrix_structure)
plt.savefig("Pictures/DLA_eta_{}".format(eta))
plt.show()
