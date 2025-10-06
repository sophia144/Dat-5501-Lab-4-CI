#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import random

def generate_data(slope_m, intercept_c):
    #generating x values
    x_coordinates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    for x_index in range(0, len(x_coordinates)):
        x_coordinates[x_index] = x_coordinates[x_index] + random.uniform(-1, 1)
    x_coordinates = np.array(x_coordinates)

    #generating random y values
    y_coordinates_list = []
    for coordinate in x_coordinates:
        y_coordinates_list.append(coordinate * slope_m + intercept_c + random.uniform(-1, 1))
    y_coordinates = np.array(y_coordinates_list)

    #writing to the csv
    all_coordinates = np.vstack((x_coordinates, y_coordinates))
    np.savetxt('coordinates.csv', all_coordinates)
