import numpy as np
from itertools import product
import math as m


def snail(map_):
    if not map_[0]:
        return []
    directions = [1, 1, 0, 0]  # forward / backward
    rows_cols = [np.asarray(map_), np.asarray(map_).T]
    dim = len(rows_cols[0])
    depth = m.ceil(dim / 2)
    snail_ = []
    for i, j in product(range(4 * depth), range(dim)):
        y = i % 4
        reps = i // 4           # current depth
        indices = [reps, -(reps + 1),
                   -(reps + 1), reps]  # first/last
        patterns = [[reps, dim-reps], [reps+1, dim-reps],
                    [reps+1, dim-reps], [reps+1, dim-(reps+1)]]
        dir = directions[i % 4]
        idx = indices[i % 4]
        form = i % 2  # row / col
        if dir:
            if j in range(patterns[y][0], patterns[y][1]):
                snail_.append(rows_cols[form][idx % dim][j])
        else:
            if j in range(patterns[y][0], patterns[y][1]):
                snail_.append(rows_cols[form][idx % dim][-j - 1])
    return snail_
