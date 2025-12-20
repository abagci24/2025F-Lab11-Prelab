import unittest
from q1 import print_operation

class TestArithmeticOperations(unittest.TestCase):
    def test_basic_operations(self):
        self.assertEqual(print_operation("5", "3", "+"), "5 + 3 = 8")
        self.assertEqual(print_operation("5", "3", "-"), "5 - 3 = 2")
        self.assertEqual(print_operation("5", "3", "*"), "5 * 3 = 15")
        self.assertEqual(print_operation("5", "3", "/"), "5 / 3 = 1.6666666666666667")

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            print_operation("a", "3", "+")
        with self.assertRaises(ValueError):
            print_operation("5", "b", "*")

    def test_invalid_operation(self):
        with self.assertRaises(ValueError):
            print_operation("5", "3", "%")

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            print_operation("5", "0", "/")

if __name__ == '__main__':
    unittest.main()
