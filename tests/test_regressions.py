"""Проверки границ решета и корректности римского конвертера."""

import runpy
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
PRIMES = runpy.run_path(str(BASE / "Лекция 1/05_prime_numbers.py"))
ROMAN = runpy.run_path(str(BASE / "Лекция 2/05_roman_converter.py"))


class RegressionTests(unittest.TestCase):
    def test_sieve_boundaries(self):
        for limit in (-10, 0, 1):
            with self.subTest(limit=limit):
                self.assertEqual(PRIMES["prime_numbers"](limit), [])
        self.assertEqual(PRIMES["prime_numbers"](2), [2])
        self.assertEqual(PRIMES["prime_numbers"](10), [2, 3, 5, 7])

    def test_roman_round_trip(self):
        for number in range(1, 4000):
            self.assertEqual(
                ROMAN["from_roman"](ROMAN["to_roman"](number)), number
            )

    def test_invalid_roman(self):
        for text in ("", "IIII", "VX", "IC", "MMMM", "hello", "I V"):
            with self.subTest(text=text):
                with self.assertRaises(ValueError):
                    ROMAN["from_roman"](text)
        self.assertEqual(ROMAN["from_roman"]("  xlii  "), 42)

    def test_invalid_arabic(self):
        for value in (0, -1, 4000, 1.5, True):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    ROMAN["to_roman"](value)
