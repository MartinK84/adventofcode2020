import numpy as np

# load data
data = np.loadtxt('input.txt')



## Part 1
# solve using broadcasting
sum = data.reshape(len(data), 1) + data.reshape(1, len(data))
index = np.where(sum == 2020)
values = data[index[0]]
prod = np.prod(values)

# output
print(f'the product of {values[0]} and {values[1]} is {prod:0.0f}')



## Part 2
# solve using broadcasting
sum = data.reshape(len(data), 1, 1) + data.reshape(1, len(data), 1) + data.reshape(1, 1, len(data))
index = np.where(sum == 2020)
values = np.unique(data[index[0]])
prod = np.prod(values)

# output
print(f'the product of {values[0]} and {values[1]} and {values[2]} is {prod:0.0f}')
