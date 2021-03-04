from RDS_constants import n_size, initial_u, initial_v, D_u, D_v, omega, constant_diff_u, constant_diff_v
import numpy as np
import random


def initialise_conc(fluid, noise=False):
    # Create the grid and fill the grid with the initial value, depending on the fluid
    # Also add if specified noise to the grid (noise max is 1/5 * initial concentrations)

    if fluid == "U":
        if not noise:
            grid = np.full(shape=(n_size, n_size), fill_value=initial_u)
        else:
            grid = np.zeros(shape=(n_size, n_size))
            for y in range(len(grid)):
                for x in range(len(grid)):
                    if noise:
                        grid[y][x] = initial_u + 0.5 * initial_u * (0.5 - random.random())
                    else:
                        grid[y][x] = initial_u
    elif fluid == "V":
        grid = np.zeros(shape=(n_size, n_size))
        for y in range(len(grid)):
            for x in range(len(grid)):
                if 1 / 3 * n_size < y < 2 / 3 * n_size and 1 / 3 * n_size < x < 2 / 3 * n_size:
                    if noise:
                        grid[y][x] = initial_v + 0.5 * initial_v * (0.5 - random.random())
                    else:
                        grid[y][x] = initial_v
    else:
        raise ValueError('Fluid does not exist.')
    return grid


def neighbour_conc(concentrations, j, i):
    # give the sum of the concentration of the neighbours

    neighbour_values = concentrations[j - 1][i] + concentrations[(j + 1) % n_size][i] + \
                       concentrations[j][i - 1] + concentrations[j][(i + 1) % n_size]
    return neighbour_values


def update_conc(concentration_u, concentration_v, f_u, k):
    # Let the concentrations interact and update them

    for y in range(len(concentration_u)):
        for x in range(len(concentration_u)):
            reaction_uv = concentration_u[y][x] * concentration_v[y][x] ** 2
            neighbours_u = neighbour_conc(concentration_u, y, x)
            neighbours_v = neighbour_conc(concentration_v, y, x)
            concentration_u[y][x] = concentration_u[y][x] + constant_diff_u * (
                    neighbours_u - 4 * concentration_u[y][x]) - \
                                    reaction_uv + f_u * (1 - concentration_u[y][x])
            concentration_v[y][x] = concentration_v[y][x] + constant_diff_v * (
                    neighbours_v - 4 * concentration_v[y][x]) + \
                                    reaction_uv - (f_u + k) * concentration_v[y][x]
    return concentration_u, concentration_v
