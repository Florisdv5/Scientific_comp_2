import numpy as np
from DLA_constants import omega, n_size


def find_candidates(grid, y, x):
    if grid[y][x] == 1:
        return False
    no_particles = False
    # print("YX:",y, x)
    for y2 in range(y - 1, y + 2):
        if y2 >= 0 and y2 <= len(grid) - 1:
            if grid[y2][x] == 1:
                return True
    for x2 in range(x - 1, x + 2):
        if x2 >= 0 and x2 <= len(grid) - 1:
            if grid[y][x2] == 1:
                return True
    return no_particles


def find_neighbours(object_structure):
    # Return a list of all the possible neighbours
    top_reached = False
    neighbours = []
    for j in range(0, n_size):  # Iterate through y
        for i in range(0, n_size):  # Iterate through x
            if object_structure[n_size - 1][i] == 1:
                top_reached = True
            if object_structure[j][i] == 1:
                continue
            elif j == n_size - 1:
                if object_structure[j - 1][i] == 1 or object_structure[j][(i + 1) % n_size] == 1 or\
                        object_structure[j][i - 1] == 1:
                    neighbours.append([j, i])
            elif j == 0:
                if object_structure[j + 1][i] == 1 or object_structure[j][(i + 1) % n_size] == 1 or\
                        object_structure[j][i - 1] == 1:
                    neighbours.append([j, i])
            elif object_structure[j + 1][i] == 1 or object_structure[j - 1][i] == 1 or \
                    object_structure[j][(i + 1) % n_size] == 1 or object_structure[j][i - 1] == 1:
                neighbours.append([j, i])
    return neighbours, top_reached


def concentration_neighbours(neighbours, matrix_concentration):
    # create a list with all concentrations from the possible neighbours

    conc = []
    for i in range(len(neighbours)):
        concentration_ind = matrix_concentration[neighbours[i][0]][neighbours[i][1]]
        conc.append(concentration_ind)
    return conc


def select_value(probs):
    options = []
    value = np.random.choice(probs, p=probs)
    for x in range(len(probs)):
        if probs[x] == value:
            options.append(x)
    return np.random.choice(options)


def initialise_grid():
    # Initialise the grid with the analytical solution for an n x n grid

    grid = np.zeros(shape=(n_size, n_size))
    for y in range(n_size):
        y_value = y / n_size
        for x in range(n_size):
            grid[y][x] = y_value
    return grid


def update_SOR(object_structure, concentrations):
    # Update the concentration matrix with SOR

    global omega
    grid_this_time = concentrations.copy()
    for j in range(0, n_size):  # Iterate through y
        for i in range(0, n_size):  # Iterate through x
            if j == 0:
                grid_this_time[j][i] = 0
            elif j == n_size - 1:
                grid_this_time[j][i] = 1
            elif object_structure[j][i] == 1:
                grid_this_time[j][i] = 0
            else:
                neighbour_values = grid_this_time[j - 1][i] + grid_this_time[j + 1][i] + \
                                   grid_this_time[j][i - 1] + grid_this_time[j][(i + 1) % n_size]
                grid_this_time[j][i] = omega / 4 * neighbour_values + (1 - omega) * grid_this_time[j][i]
    return grid_this_time

def update_SOR_omega(object_structure, concentrations, omega):
    # Update the concentration matrix with SOR

    grid_this_time = concentrations.copy()
    for j in range(0, n_size):  # Iterate through y
        for i in range(0, n_size):  # Iterate through x
            if j == 0:
                grid_this_time[j][i] = 0
            elif j == n_size - 1:
                grid_this_time[j][i] = 1
            elif object_structure[j][i] == 1:
                grid_this_time[j][i] = 0
            else:
                neighbour_values = grid_this_time[j - 1][i] + grid_this_time[j + 1][i] + \
                                   grid_this_time[j][i - 1] + grid_this_time[j][(i + 1) % n_size]
                grid_this_time[j][i] = omega / 4 * neighbour_values + (1 - omega) * grid_this_time[j][i]
    return grid_this_time