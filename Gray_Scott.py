from RDS_constants import n_size, steps, f_u, k, f_u_list, k_list
from Gray_Scott_func import initialise_conc, update_conc
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import time
import matplotlib.animation as animation

# Question D
y_values = np.linspace(0, 1, num=n_size + 1)

# matrix_conc_u = initialise_conc("U", noise=False)
# matrix_conc_v = initialise_conc("V", noise=False)
# for step in tqdm(range(steps)):
#     matrix_conc_u, matrix_conc_v = update_conc(matrix_conc_u, matrix_conc_v, f_u, k)
# fig = plt.figure()
# ax = fig.add_subplot(111, axisbelow=True)
# f = ax.pcolormesh(y_values, y_values, matrix_conc_v)
# ax.set_xlabel("X-value", size=20)
# ax.set_ylabel("Y-value", size=20)
# for tick in ax.xaxis.get_major_ticks():
#     tick.label.set_fontsize(15)
# for tick in ax.yaxis.get_major_ticks():
#     tick.label.set_fontsize(15)
# fig.colorbar(f, ax=ax)
# plt.tight_layout()
# plt.savefig("Pictures/Gray_Scott_steps_{}_f_{}_k_{}_plot.png".format(steps, f_u, k))
# plt.show()
# Plot for different for different f & k

# Default plot with noise

fig = plt.figure(figsize=(9, 6))
axes = fig.subplots(2, 2, sharex=True, sharey=True)
fig.add_subplot(111, frameon=False)
plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
plt.grid(False)
plt.xlabel("X-value", size=15)
plt.ylabel("Y-value", size=15)
axes_num = 0
for row in axes:
    for col in row:
        matrix_conc_u = initialise_conc("U", noise=True)
        matrix_conc_v = initialise_conc("V", noise=True)
        for step in tqdm(range(steps)):
            matrix_conc_u, matrix_conc_v = update_conc(matrix_conc_u, matrix_conc_v, f_u, k)
        axes_num += 1
        col.pcolormesh(y_values, y_values, matrix_conc_v)
        # col.set_title('f = {}, k = {}'.format(round(f_u, 3), round(k, 3)))
plt.savefig("Pictures/GS_list_noise_default_9_noise_0.5.png")
plt.show()

# Plot for different for different f & k

# fig = plt.figure(figsize=(9, 6))
# axes = fig.subplots(3, 3, sharex=True, sharey=True)
# fig.add_subplot(111, frameon=False)
# plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
# plt.grid(False)
# plt.xlabel("X-value", size=15)
# plt.ylabel("Y-value", size=15)
# axes_num = 0
# for row in axes:
#     for col in row:
#         f_u = f_u_list[axes_num]
#         k = k_list[axes_num]
#         matrix_conc_u = initialise_conc("U", noise=False)
#         matrix_conc_v = initialise_conc("V", noise=False)
#         for step in tqdm(range(steps)):
#             matrix_conc_u, matrix_conc_v = update_conc(matrix_conc_u, matrix_conc_v, f_u, k)
#         axes_num += 1
#         col.pcolormesh(y_values, y_values, matrix_conc_v)
#         col.set_title('f = {}, k = {}'.format(round(f_u, 3), round(k, 3)))
# plt.savefig("Pictures/GS_list_9")
# plt.show()

# GIF animation creator

# fig = plt.figure()
# plts = []
# i = 0
# matrix_conc_u = initialise_conc("U", noise=False)
# matrix_conc_v = initialise_conc("V", noise=False)
# for step in tqdm(range(steps)):
#     matrix_conc_u, matrix_conc_v = update_conc(matrix_conc_u, matrix_conc_v, f_u, k)
#     if step < 10 or step % 20 == 0:
#         p = plt.pcolormesh(y_values, y_values, matrix_conc_v)
#         plts.append([p])
#         i += 1
# print("Amount of plots created: " + str(i))
# fig.colorbar(p)
# plt.xlabel("X-value", size=15)
# plt.ylabel("Y-value", size=15)
# ani = animation.ArtistAnimation(fig, plts, interval=10, repeat_delay=10)
# # plt.show()
# writergif = animation.PillowWriter(fps=10)
# ani.save("Pictures/Animation_conc_V_{}.gif".format(steps), writer=writergif)
