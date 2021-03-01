def update_SOR(grid_last_time):
    global omega
    grid_this_time = grid_last_time.copy()
    for j in range(0, n_intervals + 1):  # Iterate through y
        for i in range(0, n_intervals + 1):  # Iterate through x
            if j == 0:
                grid_this_time[j][i] = 0
            elif j == n_intervals:
                grid_this_time[j][i] = 1
            else:
                neighbour_values = grid_this_time[j - 1][i] + grid_this_time[j + 1][i] + \
                                   grid_this_time[j][i - 1] + grid_this_time[j][(i + 1) % (n_intervals+1)]
                grid_this_time[j][i] = omega / 4 * neighbour_values + (1 - omega) * grid_this_time[j][i]
    return grid_this_time