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
