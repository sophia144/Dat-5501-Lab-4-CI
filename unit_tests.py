#import necessary libraries
import unittest
import numpy as np
import matplotlib.pyplot as plt
import random

#imports functions from other files
from best_fit_function import create_best_fit
from data_generation import generate_data

class fit_checks(unittest.TestCase):
    def test_unit(self):
       generate_data(8, 2)
       function_output = create_best_fit()
       expected_output = [8, 2]
       self.assertEqual(function_output, expected_output, f"Fail: expected {expected_output}, got {function_output}")


if __name__ == '__main__':
    unittest.main()
