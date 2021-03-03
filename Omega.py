import numpy as np
from SOR_funcs import update_SOR_omega, initialise_grid, find_neighbours, concentration_neighbours
import matplotlib.pyplot as plt
from DLA_constants import n_size, steps, eta, eta_list


def one_step_omega(matrix_structure, matrix_concentration,omega):
    matrix_concentration = update_SOR_omega(matrix_structure, matrix_concentration,omega)
    neighbours, top_reached = find_neighbours(matrix_structure)
    neighbours_conc = concentration_neighbours(neighbours, matrix_concentration)
    sum_candidates_conc = 0
    for i in range(len(neighbours_conc)):
        if neighbours_conc[i] <= 0:
            neighbours_conc[i] = 0
        else:
            sum_candidates_conc += neighbours_conc[i] ** eta
    probabilities = []
    for i in range(len(neighbours_conc)):
        if neighbours_conc[i] == 0:
            probabilities.append(0)
        else:
            probabilities.append(neighbours_conc[i] ** eta / sum_candidates_conc)
    choice = np.random.choice(len(neighbours), p=probabilities)
    added_neighbour = neighbours[choice]
    matrix_structure[added_neighbour[0]][added_neighbour[1]] = 1
    return matrix_structure, matrix_concentration, top_reached

omega_list = np.linspace(0, 2, 10)
step_list = np.zeros(shape=(len(eta_list), len(omega_list)))
for eta_i in range(len(eta_list)):
    for omega_i in range(len(omega_list)):
        eta = eta_list[eta_i]
        omega = omega_list[omega_i]
        matrix_structure = np.zeros(shape=(n_size, n_size))
        matrix_structure[0][int(n_size / 2)] = 1
        matrix_concentration = initialise_grid()
        step = 0
        top_reached = False
        while top_reached == False:
            matrix_structure, matrix_concentration, top_reached = one_step_omega(matrix_structure, matrix_concentration,omega)
            step += 1
        step_list[eta_i][omega_i] = step

lowest_omega_list = [0]*len(eta_list)

for eta_i in range(len(eta_list)):
    step = step_list[eta_i][0]
    for omega_i in range(1, len(omega_list)):
        if step_list[eta_i][omega_i] < step:
            step = step_list[eta_i][omega_i]
            lowest_omega_list[eta_i] = omega_list[omega_i]

fig = plt.figure(figsize=(9, 6))
plt.plot(eta_list, lowest_omega_list)
plt.xlabel('$\eta$')
plt.ylabel('Ideal $\omega$')
#plt.savefig("Pictures/Amount_of_steps_top")
plt.show()