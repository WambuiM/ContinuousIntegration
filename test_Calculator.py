import unittest
import Calculator


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(Calculator.addition(5, 5), 10)
        self.assertEqual(Calculator.addition(-3, 3), 0)
        self.assertEqual(Calculator.addition(-5, -5), 10)

    def test_subtraction(self):
        self.assertEqual(Calculator.subtraction(15, 5), 10)
        self.assertEqual(Calculator.subtraction(-1, 2), -3)
        self.assertEqual(Calculator.subtraction(-1, -1), 0)
        self.assertEqual(Calculator.subtraction(-1, -3), 2)
        self.assertEqual(Calculator.subtraction(6, -9), 3)
        self.assertEqual(Calculator.subtraction(-6, 3), -3)
