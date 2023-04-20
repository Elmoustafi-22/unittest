#!/bin/python3


import unittest

from prime_number import is_prime

class TestPrime(unittest.TestCase):

    def test_three(self):
        self.assertTrue(is_prime(3))

    def test_five(self):
        self.assertTrue(is_prime(5))

    def test_prime_not_prime(self):
        self.assertTrue(is_prime(11))
        self.assertFalse(is_prime(9))

    def test_typeerror_1(self):
        with self.assertRaises(TypeError):
            is_prime(6.5)

    def test_typeerror_2(self):
        with self.assertRaises(TypeError):
            is_prime('five')

    def test_valueerror(self):
        with self.assertRaises(ValueError):
            is_prime(-4)


if __name__ == '__main__':
    unittest.main()
