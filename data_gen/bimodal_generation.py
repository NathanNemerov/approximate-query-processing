import random
import matplotlib.pyplot as plt
import numpy as np

BIAS_ARRAY = [0.01, 0.02, 0.03, 0.1, 0.2, 0.2, 0.3, 0.3, 0.4, 0.5, 0.5, 0.6, 0.8, 1, 0.8, 0.6, 0.5, 0.5, 0.4, 0.3, 0.3, 0.2, 0.2, 0.1, 0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.2, 0.3, 0.3, 0.4, 0.5, 0.5, 0.6, 0.8, 1, 0.8, 0.6, 0.5, 0.5, 0.4, 0.3, 0.3, 0.2, 0.2, 0.1, 0, 0, 0]

BIAS_ARRAY_LEN = len(BIAS_ARRAY)


data_size = int(input("Enter an integer number of data points to generate: "))

random_array = []


for i in range(0, data_size):
    random_array.append(BIAS_ARRAY[int(BIAS_ARRAY_LEN * i/data_size)] * random.randrange(100, 110))

x_points = np.array(range(0, data_size))

plt.plot(x_points, random_array)
plt.show()


