#import necessary libraries
import unittest
import numpy as np
import matplotlib.pyplot as plt
import random

#imports functions from other files
from best_fit_function import create_best_fit
from data_generation import generate_data

generate_data(8, 2)
function_output = create_best_fit()
expected_output = [8.0, 2.0]

print(expected_output)
print(function_output)

class fit_checks(unittest.TestCase):

    def test_both_positive(self):
       generate_data(8, 2)
       function_output = create_best_fit()
       expected_output = [8, 2]
       self.assertAlmostEqual(function_output[0], expected_output[0], 0, f"Fail: expected {expected_output[0]}, got {function_output[0]}")
       self.assertAlmostEqual(function_output[1], expected_output[1], 0, f"Fail: expected {expected_output[1]}, got {function_output[1]}")

if __name__ == '__main__':
    unittest.main()
