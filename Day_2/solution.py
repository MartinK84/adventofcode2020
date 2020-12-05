import numpy as np

# load data
data = np.loadtxt('Day_2\input.txt', dtype=str)

## Part 1
limits = np.char.split(data[:,0],'-')
ind_1 = [int(x[0]) for x in limits]
ind_2 = [int(x[1]) for x in limits]
letter = [x[0] for x in data[:,1]]
counts = [np.char.count(x, l) for x, l in zip(data[:,2], letter)]
valid = [(x >= mi) and (x <= ma) for x, mi, ma in zip(counts, ind_1, ind_2)]
print(np.count_nonzero(valid))

## Part 2
valid = [((passwd[i1 - 1] == l) and not (passwd[i2 - 1] == l)) or ((passwd[i2 - 1] == l) and not (passwd[i1 - 1] == l)) for passwd, l, i1, i2 in zip(data[:,2], letter, ind_1, ind_2)]
print(np.count_nonzero(valid))