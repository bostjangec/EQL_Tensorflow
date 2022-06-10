import gzip
import pickle

import numpy as np

from utils import to_float32, number_of_positional_arguments
filename = 'data/F1data_train_val'
filename = 'data/F1dataN_train_val'
data = to_float32(pickle.load(gzip.open(filename, "rb"), encoding='latin1'))
print(type(data))
# print(len(data))

# create lorenz

from ProGED.examples.DS2022.generate_data_ODE_systems import generate_ODE_data, lorenz, lorenz_stable, VDP

system = 'VDP'
inits = [-0.2, -0.8]
data = generate_ODE_data(lorenz_stable, [1,1,1])

print(type(data))

