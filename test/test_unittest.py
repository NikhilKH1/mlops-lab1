import sys
import os
import unittest

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src import calculator


class TestCalculator(unittest.TestCase):

    def test_fun1(self):
        self.assertEqual(calculator.fun1(2, 3), 5)
        self.assertEqual(calculator.fun1(5, 0), 5)
        
        self.assertEqual(calculator.fun1(-1, 1), 0)
        self.assertEqual(calculator.fun1(-1, -1), -2)

    def test_fun2(self):
        self.assertEqual(calculator.fun2(2, 3), -1)
        self.assertEqual(calculator.fun2(5, 0), 5)
        self.assertEqual(calculator.fun2(-1, 1), -2)
        self.assertEqual(calculator.fun2(-1, -1), 0)

    def test_fun3(self):
        self.assertEqual(calculator.fun3(2, 3), 6)
        self.assertEqual(calculator.fun3(5, 0), 0)
        self.assertEqual(calculator.fun3(-1, 1), -1)
        self.assertEqual(calculator.fun3(-1, -1), 1)

    def test_fun4(self):
        self.assertEqual(calculator.fun4(2, 3, 5), 10)
        self.assertEqual(calculator.fun4(5, 0, -1), 4)
        self.assertEqual(calculator.fun4(-1, -1, -1), -3)
        self.assertEqual(calculator.fun4(-1, -1, 100), 98)

    def test_fun5(self):
        self.assertEqual(calculator.fun5(10, 2), 5)
        self.assertEqual(calculator.fun5(5, 2), 2.5)
        self.assertEqual(calculator.fun5(-10, 2), -5)
        self.assertEqual(calculator.fun5(0, 5), 0)

    def test_fun5_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.fun5(10, 0)

    def test_fun6(self):
        # Power
        self.assertEqual(calculator.fun6(2, 3), 8)
        self.assertEqual(calculator.fun6(5, 0), 1)
        self.assertEqual(calculator.fun6(-2, 2), 4)
        self.assertEqual(calculator.fun6(10, 2), 100)

    def test_fun7(self):
        # Modulus
        self.assertEqual(calculator.fun7(10, 3), 1)
        self.assertEqual(calculator.fun7(8, 2), 0)
        self.assertEqual(calculator.fun7(5, 2), 1)
        self.assertEqual(calculator.fun7(15, 4), 3)

    def test_fun7_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.fun7(10, 0)

    def test_fun8(self):
        # Average
        self.assertEqual(calculator.fun8(10, 20, 30), 20)
        self.assertEqual(calculator.fun8(1, 2, 3), 2)
        self.assertEqual(calculator.fun8(-1, -2, -3), -2)
        self.assertEqual(calculator.fun8(0, 0, 0), 0)

    def test_fun9(self):
        # Maximum
        self.assertEqual(calculator.fun9(10, 20, 5), 20)
        self.assertEqual(calculator.fun9(-1, -2, -3), -1)
        self.assertEqual(calculator.fun9(5, 5, 5), 5)
        self.assertEqual(calculator.fun9(100, 0, 50), 100)

    def test_fun10(self):
        # Minimum
        self.assertEqual(calculator.fun10(10, 20, 5), 5)
        self.assertEqual(calculator.fun10(-1, -2, -3), -3)
        self.assertEqual(calculator.fun10(5, 5, 5), 5)
        self.assertEqual(calculator.fun10(100, 0, 50), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            calculator.fun1("2", 3)

        with self.assertRaises(ValueError):
            calculator.fun2(2, "3")

        with self.assertRaises(ValueError):
            calculator.fun3("2", 3)

        with self.assertRaises(ValueError):
            calculator.fun4(1, "2", 3)

        with self.assertRaises(ValueError):
            calculator.fun5("10", 2)

        with self.assertRaises(ValueError):
            calculator.fun6(2, "3")

        with self.assertRaises(ValueError):
            calculator.fun7("10", 3)

        with self.assertRaises(ValueError):
            calculator.fun8(1, "2", 3)

        with self.assertRaises(ValueError):
            calculator.fun9(1, 2, "3")

        with self.assertRaises(ValueError):
            calculator.fun10("1", 2, 3)



if __name__ == '__main__':
    unittest.main()