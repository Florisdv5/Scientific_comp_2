from DLA_constants import n_size, prob_s_list, steps, prob_s
import numpy as np
import random
import matplotlib.pyplot as plt
from tqdm import tqdm


def new_walker():
    new_location_x = random.choice(range(n_size))
    walker = [n_size-1, new_location_x]
    return walker


def step(walker, object):
    # walker must not walk over object
    possib_moves = []
    if object[walker[0]][walker[1]-1] == 0:
        possib_moves.append("left")
    if object[walker[0]][(walker[1]+1) % n_size] == 0:
        possib_moves.append("right")
    if walker[0] == n_size-1:
        possib_moves.append("down")
    elif object[walker[0]+1][walker[1]] == 0:
        possib_moves.append("down")
    if walker[0] == 0:
        possib_moves.append("up")
    elif object[walker[0]-1][walker[1]] == 0:
        possib_moves.append("up")
    move = random.choice(possib_moves)
    if move == "left":
        walker[1] -= 1
    if move == "right":
        walker[1] += 1
    if move == "up":
        walker[0] -= 1
    if move == "down":
        walker[0] += 1
    walker[1] = walker[1] % n_size
    return walker


def check_stop(walker,object):
    if walker[0] == 0:
        neighbours = [walker[:], walker[:], walker[:]]
        neighbours[0][0] += 1
        neighbours[1][1] += 1
        neighbours[2][1] -= 1
    elif walker[0] == n_size-1:
        neighbours = [walker[:], walker[:], walker[:], walker[:]]
        neighbours[0][0] -= 1
        neighbours[1][1] += 1
        neighbours[2][1] -= 1
    else:
        neighbours = [walker[:], walker[:], walker[:], walker[:]]
        neighbours[0][0] += 1
        neighbours[1][0] -= 1
        neighbours[2][1] += 1
        neighbours[3][1] -= 1
    stop = 0
    for i in range(len(neighbours)):
        if object[neighbours[i][0]][neighbours[i][1]%n_size] == 1:
            if prob_s > random.random():
                stop = 1
            # print("Stop", walker)
    return stop


# Simulation for question B

# grid = np.zeros(shape=(n_size, n_size))
# grid[0][int(n_size / 2)] = 1
# for i in tqdm(range(steps)):
#     walker = new_walker()
#     while check_stop(walker, grid) == 0:
#         walker = step(walker, grid)
#         if walker[0] < 0 or walker[0] > n_size-1:
#             walker = new_walker()
#     grid[walker[0]][walker[1]] = 1
# y_values = np.linspace(0, 1, num=n_size+1)
# plt.pcolormesh(y_values, y_values, grid)
# plt.savefig("Pictures/MC_tree_prob_{}".format(prob_s))
# plt.show()

# Simulation for question C

y_values = np.linspace(0, 1, num=n_size+1)
fig = plt.figure(figsize=(9, 6))
axes = fig.subplots(2, 2, sharex = True, sharey = True)
fig.add_subplot(111, frameon=False)
plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
plt.grid(False)
plt.xlabel("X-value", size = 15)
plt.ylabel("Y-value", size = 15)
axes_num = 0
for row in axes:
    for col in row:
        prob_s = prob_s_list[axes_num]
        grid = np.zeros(shape=(n_size, n_size))
        grid[0][int(n_size / 2)] = 1
        axes_num += 1
        for i in tqdm(range(steps)):
            walker = new_walker()
            while check_stop(walker, grid) == 0:
                walker = step(walker, grid)
                if walker[0] < 0 or walker[0] > n_size-1:
                    walker = new_walker()
            grid[walker[0]][walker[1]] = 1
        col.pcolormesh(y_values, y_values, grid)
        col.set_title(r'$p_s = {}$'.format(prob_s))
plt.savefig("Pictures/MC_tree_prob_list")
plt.show()
