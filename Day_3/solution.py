import numpy as np
from numpy.core.fromnumeric import prod

# load data
data = np.genfromtxt('Day_3\input.txt', dtype=str, comments=None)

## Part 1

# build index list
step_x = 3
step_y = 1
ind_y = np.linspace(0, len(data) - 1, len(data)).astype(int)
ind_x = np.arange(0, len(data) * step_x, step_x)
ind_x = np.mod(ind_x, len(data[0])).astype(int)
ind_lin = np.ravel_multi_index((ind_x[1:], ind_y[1:]), (len(data[0]), len(data)), order='F')

# get data for index positions
data_lin = np.array([y for x in data for y in x])
data_ind = data_lin[ind_lin.astype(int)]
print(np.count_nonzero(data_ind == '#'))

## Part 2
step_list = np.array([(1,1), (3,1), (5,1), (7,1), (1,2)])
counts = np.zeros((5))
nCount = 0
for step in step_list:
    # build index list
    step_x = step[0]
    step_y = step[1]
    ind_y = np.arange(0, len(data), step_y)
    ind_x = np.arange(0, len(data) * step_x, step_x)
    ind_x = np.mod(ind_x, len(data[0])).astype(int)
    ind_x = ind_x[0:len(ind_y)]
    ind_lin = np.ravel_multi_index((ind_x[1:], ind_y[1:]), (len(data[0]), len(data)), order='F')

    # get data for index positions
    data_lin = np.array([y for x in data for y in x])
    data_ind = data_lin[ind_lin.astype(int)]
    counts[nCount] = np.count_nonzero(data_ind == '#')
    nCount += 1

print(counts)
print(np.prod(counts))