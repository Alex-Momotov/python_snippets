# It is a naming convention to name the test class with 'test_class_to_be_tested'

import unittest
import calc

# We begin by creating a class and inheriting from unittest.TestCase
# Testing methods defined in this class must start with 'test_'

# In order to actually run the unittest we need to pass to the command line the following statement:
#       "python -m unittest test_calc.py"
class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)
        with self.assertRaises(ValueError):
            calc.divide(10, 0)

# If we want to avoid running our tests from the command line, we can set up this shortcut here:
if __name__ == '__main__':
    unittest.main()