import numpy as np

n_size = 100
dt = 1
dx = 1
D_u = 0.16
D_v = 0.08
f_u = 0.035
f_u_list = [0.020, 0.020, 0.020, 0.035, 0.035, 0.035, 0.050, 0.050, 0.050]
k = 0.06
k_list = [0.04, 0.06, 0.08, 0.04, 0.06, 0.08, 0.04, 0.06, 0.08]
initial_u = 0.5
initial_v = 0.25
steps = 5000
omega = 1
constant_diff_u = dt*D_u/dx**2
constant_diff_v = dt*D_v/dx**2
print("Constant u must be below 1 and is: " + str(constant_diff_u*4))
print("Constant v must be below 1 and is: " + str(constant_diff_v*4))