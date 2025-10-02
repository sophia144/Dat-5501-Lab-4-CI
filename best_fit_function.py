#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import random

#generating x values
x_coordinates = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

#taking inputs
slope_m = float(input("Input gradient:\n"))
intercept_c = float(input("Input intercept:\n"))

#generating random y values
y_coordinates_list = []
for coordinate in x_coordinates:
    y_coordinates_list.append(coordinate * slope_m + intercept_c + random.randint(1,5))
y_coordinates = np.array(y_coordinates_list)

#create plot
plt.scatter(x_coordinates, y_coordinates, color='blue', label='Example Data')

#generate the best-fit line
coefficients = np.polyfit(x_coordinates, y_coordinates, 1)  # 1 means linear
slope, intercept = coefficients
best_fit_line = slope * x_coordinates + intercept

#plot the best-fit line
plt.plot(x_coordinates, best_fit_line, color='pink', label='Best Fit Line')

#adding labels and legends
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Example Data')
plt.legend()

#output the graph
plt.show()
