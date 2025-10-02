import unittest
from subtraction_function import subtract_numbers


class subtraction_checks(unittest.TestCase):
    def test_unit(self):

        function_output = subtract_numbers(8, 2)
        expected_output = 6
        self.assertEqual(function_output, expected_output, f"Fail: expected {expected_output}, got {function_output}")

        function_output = subtract_numbers(-24, 5)
        expected_output = -29
        self.assertEqual(function_output, expected_output, f"Fail: expected {expected_output}, got {function_output}")

        function_output = subtract_numbers(-6, -7)
        expected_output = 1
        self.assertEqual(function_output, expected_output, f"Fail: expected {expected_output}, got {function_output}")


if __name__ == '__main__':
    unittest.main()
