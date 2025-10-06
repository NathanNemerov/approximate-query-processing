import random
import matplotlib.pyplot as plt
import numpy as np

BIAS_ARRAY = [
    0.0,    0.0773, 0.2044, 0.3453, 0.4834, 0.6077, 0.7155, 0.8039,
    0.8729, 0.9254, 0.9613, 0.9862, 0.9972, 1.0,    0.9945, 0.9807,
    0.9641, 0.942,  0.9171, 0.8895, 0.8619, 0.8343, 0.8039, 0.7762,
    0.7459, 0.7182, 0.6906, 0.663,  0.6354, 0.6105, 0.5856, 0.5608,
    0.5359, 0.5138, 0.4917, 0.4724, 0.453,  0.4337, 0.4144, 0.3978,
    0.3812, 0.3646, 0.3508, 0.3343, 0.3204, 0.3094, 0.2956, 0.2845,
    0.2735, 0.2624, 0.2514, 0.2431, 0.232,  0.2238
]

BIAS_ARRAY_LEN = len(BIAS_ARRAY)


data_size = int(input("Enter an integer number of data points to generate: "))

random_array = []

for i in range (0, data_size):
    random_array.append(BIAS_ARRAY[int(BIAS_ARRAY_LEN * i/data_size)] * random.randrange(100, 110))

x_points = np.array(range(0, data_size))

plt.plot(x_points, random_array)
plt.show()