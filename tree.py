import numpy as np
from SOR_funcs import update_SOR, initialise_grid, find_neighbours, concentration_neighbours, max_difference
import matplotlib.pyplot as plt
from tqdm import tqdm
from DLA_constants import n_size, steps, eta, eta_list, epsilon
import time


def one_step(matrix_structure, matrix_concentration):
    difference = 1
    while difference > epsilon:
        old_matrix_concentration = matrix_concentration.copy()
        matrix_concentration = update_SOR(matrix_structure, matrix_concentration)
        difference = max_difference(matrix_concentration, old_matrix_concentration)
        print(difference)
    print("YEE")
    neighbours, top_reached = find_neighbours(matrix_structure)
    neighbours_conc = concentration_neighbours(neighbours, matrix_concentration)

    sum_candidates_conc = 0
    for i in range(len(neighbours_conc)):
        sum_candidates_conc += neighbours_conc[i] ** eta
    probabilities = []
    for i in range(len(neighbours_conc)):
        probabilities.append(neighbours_conc[i] ** eta / sum_candidates_conc)

    choice = np.random.choice(len(neighbours), p=probabilities)
    added_neighbour = neighbours[choice]
    matrix_structure[added_neighbour[0]][added_neighbour[1]] = 1
    return matrix_structure, matrix_concentration, top_reached


# Question B
#
# y_values = np.linspace(0, 1, num=n_size + 1)
# matrix_structure = np.zeros(shape=(n_size, n_size))
# matrix_structure[0][int(n_size / 2)] = 1
# matrix_concentration = initialise_grid()
# step = 0
# top_reached = False
# while step < steps and top_reached == False:
#     matrix_structure, matrix_concentration, top_reached = one_step(matrix_structure, matrix_concentration)
#     step += 1
# print(step)
# fig = plt.figure()
# ax = fig.add_subplot(111, axisbelow=True)
# ax.pcolormesh(y_values, y_values, matrix_structure)
# ax.set_xlabel("X-value", size=20)
# ax.set_ylabel("Y-value", size=20)
# for tick in ax.xaxis.get_major_ticks():
#     tick.label.set_fontsize(15)
# for tick in ax.yaxis.get_major_ticks():
#     tick.label.set_fontsize(15)
# plt.tight_layout()
# plt.savefig("Pictures/DLA_eta_{}".format(eta))
# plt.show()

# Question A

# y_values = np.linspace(0, 1, num=n_size + 1)
# fig = plt.figure(figsize=(9, 6))
# axes = fig.subplots(3, 3, sharex=True, sharey=True)
# fig.add_subplot(111, frameon=False)
# plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
# plt.grid(False)
# plt.xlabel("X-value", size=15)
# plt.ylabel("Y-value", size=15)
# axes_num = 0
# step_list = []
# for row in tqdm(axes):
#     for col in tqdm(row):
#         eta = eta_list[axes_num]
#         matrix_structure = np.zeros(shape=(n_size, n_size))
#         matrix_structure[0][int(n_size / 2)] = 1
#         matrix_concentration = initialise_grid()
#         step = 0
#         top_reached = False
#         while not top_reached and step < steps:
#             matrix_structure, matrix_concentration, top_reached = one_step(matrix_structure, matrix_concentration)
#             step += 1
#         step_list.append(step)
#         axes_num += 1
#         print(eta)
#         col.pcolormesh(y_values, y_values, matrix_structure)
#         col.set_title(r'$\eta = {}$, steps = {}'.format(round(eta, 3), step))
#
# print(step_list)
#
# # step_list = [2000, 2000, 2000, 1978, 1642, 1094, 817, 591, 530]
# plt.savefig("Pictures/DLA_eta_list_9")
# plt.show()
# # fig.clear(True)
# fig = plt.figure(figsize=(9, 6))
# plt.plot(eta_list, step_list)
# plt.xlabel('$\eta$')
# plt.ylabel('Amount of steps')
# plt.savefig("Pictures/Amount_of_steps_top")
# plt.show()

step_list_etas = [[], [], [], [], [], [], [], [], []]
for i in tqdm(range(10)):
    for eta_values in range(9):
        eta = eta_list[eta_values]
        matrix_structure = np.zeros(shape=(n_size, n_size))
        matrix_structure[0][int(n_size / 2)] = 1
        matrix_concentration = initialise_grid()
        step = 0
        top_reached = False
        while not top_reached and step < steps:
            matrix_structure, matrix_concentration, top_reached = one_step(matrix_structure, matrix_concentration)
            step += 1
        step_list_etas[eta_values].append(step)
path = 'Archives/saved_step_list_eta_{0}.npy'.format(int(time.time()))
with open(path, 'ab') as f:
    np.save(f, step_list_etas)
