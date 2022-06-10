import gzip
import pickle

import numpy as np

# EQL data_util test:
# from utils import to_float32, number_of_positional_arguments
# filename = 'data/F1data_train_val'
# filename = 'data/F1dataN_train_val'
# data = to_float32(pickle.load(gzip.open(filename, "rb"), encoding='latin1'))
# print(type(data))
# # print(len(data))



# Create lorenz

from ProGED.examples.DS2022.generate_data_ODE_systems import generate_ODE_data, lorenz, lorenz_stable, VDP

system = 'VDP'
inits = [-0.2, -0.8]
data = generate_ODE_data(lorenz_stable, [1,1,1])

x = data[:,1]
dt = data[1][0]-data[0][0]
dx =  np.gradient(x, dt)


# print(data[1])
# print(data[0])
# print(data[1][0])
# print(data[0][0])
print('dt', dt)
#




print(type(data))

