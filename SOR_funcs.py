import numpy as np


def find_candidates(grid, y, x):
    if grid[y][x] == 1:
        return False
    no_particles = False
    #print("YX:",y, x)
    for y2 in range(y - 1, y + 2):
        if y2 >= 0 and y2 <= len(grid) - 1:
            if grid[y2][x] == 1:
                return True
    for x2 in range(x - 1, x + 2):
        if x2 >= 0 and x2 <= len(grid) - 1:
            if grid[y][x2] == 1:
                return True
    return no_particles


def select_value(probs):
    options = []
    value = np.random.choice(probs, p=probs)
    for x in range(len(probs)):
        if probs[x] == value:
            options.append(x)
    return np.random.choice(options)


def calculate_SOR(old_grid, new_grid, y, x, omega):
    if y == len(old_grid) - 1:
        return omega / 4 * (new_grid[y - 1][x] + old_grid[y][x + 1] + new_grid[y][x - 1]) +\
               (1 - omega) * old_grid[y][x]
    elif y == 0:
        return omega / 4 * (old_grid[y + 1][x] + old_grid[y][x + 1] + new_grid[y][x - 1]) +\
               (1 - omega) * old_grid[y][x]
    elif x == 0:
        return omega / 4 * (old_grid[y + 1][x] + new_grid[y - 1][x] + old_grid[y][x + 1]) +\
               (1 - omega) * old_grid[y][x]
    elif x == len(old_grid[0]) - 1:
        return omega / 4 * (old_grid[y + 1][x] + new_grid[y - 1][x] + new_grid[y][x - 1]) +\
               (1 - omega) * old_grid[y][x]
    else:
        return omega / 4 * (old_grid[y + 1][x] + new_grid[y - 1][x] + old_grid[y][x + 1] + new_grid[y][x - 1]) + (1 - omega) * old_grid[y][x]