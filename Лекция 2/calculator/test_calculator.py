"""Задача 3: тест функции сложения; проверка исправления задачи 4."""

import unittest

from calculator import add_numbers, divide


class CalculatorTests(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-2, 3), 1)
        self.assertAlmostEqual(add_numbers(0.1, 0.2), 0.3)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertIsNone(divide(10, 0))


if __name__ == "__main__":
    unittest.main()
