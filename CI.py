import numpy as np
import matplotlib.pyplot as plt
from DLA_constants import eta_list, prob_s_list
import statistics
import math


def statistics_list(given_list):
    mean_list = []
    sd_list = []
    lower_bound_list = []
    upper_bound_list = []
    for list_value in range(len(given_list)):
        mean_list.append(statistics.mean(given_list[list_value]))
        sd_list.append(statistics.stdev(given_list[list_value]))
        lower_bound_list.append(mean_list[list_value] - 1.96 * sd_list[list_value] / math.sqrt(len(given_list[list_value])))
        upper_bound_list.append(mean_list[list_value] + 1.96 * sd_list[list_value] / math.sqrt(len(given_list[list_value])))
    return mean_list, sd_list, lower_bound_list, upper_bound_list


def figure_CI(list_given, reference_list, save_fig=False, path_given="Pictures/figure_CI", x_label=r'$\eta$'):
    mean_list, sd_list, lower_bound_list, upper_bound_list = statistics_list(list_given)
    fig = plt.figure()
    ax = fig.add_subplot(111, axisbelow=True)
    for value in range(len(reference_list)):
        ax.plot(reference_list, mean_list, alpha=0.6, color = 'blue', lw=2)
        ax.fill_between(x=reference_list, y1=lower_bound_list,
                        y2=upper_bound_list, color = 'blue', linewidth=0.5, alpha=0.05)
    ax.set_xlabel(x_label, size=20)
    ax.set_ylabel('Number of steps', size=20)
    ax.grid(b=True, which='major', c='lightgray', lw=2, ls='-')
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(15)
    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(15)
    plt.tight_layout()
    if save_fig:
        plt.savefig("Pictures/{}".format(path_given))
    plt.show()


path = 'Archives/saved_step_list_eta_1614939981.npy'
with open(path, 'rb') as f:
    step_list_eta = np.load(f, allow_pickle=True)[()]
figure_CI(step_list_eta, eta_list, save_fig=True, path_given="figure_step_list_CI_eta", x_label=r'$\eta$')
#
# path = 'Archives/saved_step_list_prob_s_1614865598.npy'
# with open(path, 'rb') as f:
#     step_list_prob_s = np.load(f, allow_pickle=True)[()]
# # new_array = np.array([[690, 845, 682, 804, 840, 780, 978, 682, 862, 916]])
# # step_list_prob_s = np.concatenate((step_list_prob_s, new_array), axis=0)
# # print(step_list_prob_s)
# # prob_s_list.append(1)
# figure_CI(step_list_prob_s, prob_s_list, save_fig=True, path_given="figure_step_list_CI_prob_s_with_1",
#           x_label=r'$p_s$')
