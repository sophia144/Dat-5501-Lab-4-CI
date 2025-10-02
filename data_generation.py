#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import random

#generating x values
x_coordinates = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

#taking inputs
slope_m = float(input("Input gradient:\n"))
intercept_c = float(input("Input intercept:\n"))

#generating random y values
y_coordinates_list = []
for coordinate in x_coordinates:
    y_coordinates_list.append(coordinate * slope_m + intercept_c + random.randint(1,5))
y_coordinates = np.array(y_coordinates_list)

#writing to the csv
all_coordinates = np.vstack((x_coordinates, y_coordinates))
np.savetxt('coordinates.csv', all_coordinates)