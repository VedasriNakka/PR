import numpy as np
from scipy.optimize import linear_sum_assignment

"""
to get distance between two graphs, call:
-> hungarian(dirac(g1, g2))

g1 and g2 in forms of: np.asarray([['O', 2], ['C', 3], ['H', 1], ['O', 1]])
could change it easily to: np.asarray(['O', 2, 'C', 3, 'H', 1, 'O', 1])
"""


def dirac(g1, g2):
    """
    :param g1, g2: numpy array, example: np.asarray([['O', 2], ['C', 3], ['H', 1], ['O', 1]])
    :return: cost matrix (input for hungarian)
    """
    # make g1 and g2 same length: fill with ['e', 0]
    m = max(len(g1), len(g2))
    while len(g1) != len(g2):
        if len(g1) > len(g2):
            g2 = np.vstack([g2, ['e', 0]])
        if len(g2) > len(g1):
            g1 = np.vstack([g1, ['e', 0]])
    # init and fill matrix
    cost_matrix = np.zeros((m, m))
    for i in range(m):
        for j in range(m):
            cost_matrix[i, j] = distance_calc(g1[i], g2[j])
    return cost_matrix


def hungarian(cost_matrix):
    """
    :param cost_matrix: from dirac
    :return: minimal distance (type=float)
    """
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    return cost_matrix[row_ind, col_ind].sum()


def distance_calc(p1, p2):
    diff = 0
    if p1[0] != p2[0]:
        if p1[0] == 'e' or p2[0] == 'e':
            diff += Cn
        diff += Cn
    return diff + abs(int(p1[1]) - int(p2[1])) * Ce


def hungarian_metric(g1, g2):
    cost_matrix = dirac(g1, g2)
    return hungarian(cost_matrix)


Cn = 1
Ce = .5

