from RDS_constants import n_size, initial_u, initial_v, D_u, D_v, omega, f_u, k
import numpy as np


def initialise_conc(fluid):
    if fluid == "U":
        grid = np.full(shape=(n_size, n_size), fill_value=initial_u)
    elif fluid == "V":
        grid = np.zeros(shape=(n_size, n_size))
        for y in range(len(grid)):
            for x in range(len(grid)):
                if 1/3*n_size < y < 2/3*n_size and 1/3*n_size < x < 2/3*n_size:
                    grid[y][x] = initial_v
    else:
        raise ValueError('Fluid does not exist.')
    return grid


def update_SOR(concentrations, j, i, fluid):
    # Update the concentration with SOR

    if fluid == "U":
        if j == n_size - 1:
            nabla_term = 1
        else:
            neighbour_values = concentrations[j - 1][i] + concentrations[j + 1][i] + \
                               concentrations[j][i - 1] + concentrations[j][(i + 1) % n_size]
            nabla_term = omega / 4 * neighbour_values + (1 - omega) * concentrations[j][i]
    if fluid == "V":
        neighbour_values = concentrations[j - 1][i] + concentrations[(j + 1) % n_size][i] + \
                           concentrations[j][i - 1] + concentrations[j][(i + 1) % n_size]
        nabla_term = omega / 4 * neighbour_values + (1 - omega) * concentrations[j][i]
    return nabla_term


def update_conc(concentration_u, concentration_v):
    # Let the concentrations interact and update them

    for y in range(len(concentration_u)):
        for x in range(len(concentration_u)):
            reaction_uv = concentration_u[y][x]*concentration_v[y][x]**2
            nabla_term_u = update_SOR(concentration_u, y, x, "U")
            nabla_term_v = update_SOR(concentration_v, y, x, "V")
            concentration_u[y][x] = D_u * nabla_term_u + reaction_uv + f_u * (1 - concentration_u[y][x])
            concentration_v[y][x] = D_v * nabla_term_v + reaction_uv - (f_u + k) * concentration_v[y][x]
    return concentration_u, concentration_v
