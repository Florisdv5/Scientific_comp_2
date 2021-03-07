import numpy as np
from SOR_funcs import update_SOR_omega, initialise_grid, find_neighbours, concentration_neighbours, max_difference
import matplotlib.pyplot as plt
from DLA_constants import n_size, steps, eta, eta_list, epsilon


def one_step_omega(matrix_structure, matrix_concentration,omega):
    difference = 1
    iterations = -1
    while difference > epsilon and iterations < 100:
        old_matrix_concentration = matrix_concentration.copy()
        matrix_concentration = update_SOR_omega(matrix_structure, matrix_concentration, omega)
        difference = max_difference(matrix_concentration, old_matrix_concentration)
        iterations += 1

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
    return matrix_structure, matrix_concentration, top_reached, iterations

omega_list = np.linspace(0.5, 1.8, 9)
#print(omega_list)
iteration_list = []
cut_steps = np.linspace(0,2000,21)
print(cut_steps)
# for i in range(len(cut_steps) -1):
#     iteration_list.append([])
#     top_reached = False
#     matrix_structure1 = np.zeros(shape=(n_size, n_size))
#     matrix_structure1[0][int(n_size / 2)] = 1
#     matrix_concentration1 = initialise_grid()
#     step = 0
#     while step < cut_steps[i]:
#         matrix_structure1, matrix_concentration1, top_reached, iters = one_step_omega(matrix_structure1, matrix_concentration1, 1)
#         step += 1
#     for omega_i in range(len(omega_list)):
#         step = cut_steps[i]
#         iterationsum = 0
#         matrix_structure = matrix_structure1.copy()
#         matrix_concentration = matrix_concentration1.copy()
#         #print("omega:", omega, "Before trial", matrix_concentration)
#         while step < cut_steps[i + 1]:
#             matrix_structure, matrix_concentration, top_reached, iterations = one_step_omega(matrix_structure, matrix_concentration,omega_list[omega_i])
#             step += 1
#             iterationsum += iterations
#         # print("omega:", omega, "After trial",matrix_concentration2)
#         # print(iterationsum)
#         iteration_list[i].append(iterationsum)
#         iterationsum = 0
#         print(iteration_list)

iteration_list = [[444, 477, 393, 337, 347, 346, 471, 614, 711], [418, 402, 417, 389, 460, 437, 482, 576, 841], [479, 405, 440, 404, 404, 402, 460, 632, 835], [544, 536, 460, 392, 408, 451, 510, 637, 877], [536, 487, 561, 414, 447, 403, 511, 593, 988], [457, 555, 549, 440, 412, 541, 517, 640, 1012], [707, 567, 453, 515, 453, 479, 506, 686, 977], [600, 547, 468, 424, 538, 452, 605, 688, 1096], [626, 489, 498, 460, 436, 510, 544, 725, 956], [912, 670, 651, 713, 692, 575, 683, 856, 1452], [1196, 962, 890, 898, 853, 713, 758, 1022, 1584], [1140, 1073, 1092, 989, 909, 799, 809, 930, 1547], [1032, 857, 698, 587, 641, 522, 667, 827, 1545], [1138, 1016, 1048, 956, 809, 814, 798, 943, 1471], [91, 104, 105, 95, 92, 85, 94, 71, 51], [66, 74, 71, 82, 81, 81, 63, 49, 26], [961, 916, 784, 706, 646, 633, 586, 614, 1089], [45, 48, 54, 50, 39, 23, 26, 14, 9], [48, 52, 49, 30, 28, 19, 11, 12, 5], [8, 2, 5, 0, 0, 0, 0, 0, 0]]

lowest_omega_list = []

for steps in range(len(iteration_list)):
    lowest_omega_list.append(omega_list[0])
    iterations = iteration_list[steps][0]
    for omegas in range(1, len(omega_list)):
        if iteration_list[steps][omegas] < iterations:
            iterations = iteration_list[steps][omegas]
            lowest_omega_list[steps] = omega_list[omegas]
print(lowest_omega_list)

fig = plt.figure(figsize=(9, 6))

plt.plot(cut_steps[:18], lowest_omega_list[:18])
plt.xlabel('Amount of steps', size = 15)
plt.ylabel('Ideal $\omega$', size = 15)
plt.grid(True)
plt.savefig("Pictures/ideal_omega_perf")
plt.show()