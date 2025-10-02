#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import random

def create_best_fit():
    #reading from the csv
    x_coordinates_fetched = np.array(np.loadtxt('coordinates.csv'))[0]
    y_coordinates_fetched = np.array(np.loadtxt('coordinates.csv'))[1]

    #create plot
    plt.scatter(x_coordinates_fetched, y_coordinates_fetched, color='blue', label='Example Data')

    #generate the best-fit line
    coefficients = np.polyfit(x_coordinates_fetched, y_coordinates_fetched, 1)  #1 means linear
    slope, intercept = coefficients
    best_fit_line = slope * x_coordinates_fetched + intercept

    #plot the best-fit line
    plt.plot(x_coordinates_fetched, best_fit_line, color='pink', label='Best Fit Line')

    #finds the equation of the best fit line
    m, c = np.polyfit(x_coordinates_fetched, y_coordinates_fetched, 1)
    gradient = float(m)
    intercept = float(c)

    #adding labels and legends
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Example Data')
    plt.legend()

    #output the graph
    plt.show()

    return [int(m), int(c)]

print(create_best_fit())