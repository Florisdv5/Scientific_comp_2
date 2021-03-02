from RDS_constants import n_size, steps
from Gray_Scott_func import initialise_conc, update_conc
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

# Question D
y_values = np.linspace(0, 1, num=n_size + 1)

matrix_conc_u = initialise_conc("U")
matrix_conc_v = initialise_conc("V")
for step in tqdm(range(steps)):
    matrix_conc_u, matrix_conc_v = update_conc(matrix_conc_u, matrix_conc_v)
fig = plt.figure()
ax = fig.add_subplot(111, axisbelow=True)
f = ax.pcolormesh(y_values, y_values, matrix_conc_u)
ax.set_xlabel("X-value", size=20)
ax.set_ylabel("Y-value", size=20)
for tick in ax.xaxis.get_major_ticks():
    tick.label.set_fontsize(15)
for tick in ax.yaxis.get_major_ticks():
    tick.label.set_fontsize(15)
fig.colorbar(f, ax=ax)
plt.tight_layout()
# plt.savefig("Pictures/Gray_Scott")
plt.show()