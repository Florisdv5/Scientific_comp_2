from DLA_constants import n_size, prob_s, steps
import numpy as np
import random
import matplotlib.pyplot as plt
from tqdm import tqdm

grid = np.zeros(shape=(n_size, n_size))
grid[n_size - 1][int(n_size / 2)] = 1


def new_walker():
    new_location_x = random.choice(range(n_size))
    walker = [0, new_location_x]
    return walker


def step(walker):
    moves = ["left", "right", "up", "down"]
    move = random.choice(moves)
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
            stop = 1
            # print("Stop", walker)
    return stop


for i in tqdm(range(steps)):
    walker = new_walker()
    while check_stop(walker, grid) == 0:
        walker = step(walker)
        if walker[0] < 0 or walker[0] > n_size-1:
            walker = new_walker()
    grid[walker[0]][walker[1]] = 1

plt.matshow(grid)
plt.show()
plt.savefig("Pictures/MC_tree")
