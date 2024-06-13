from unittest import TestCase

from PrimeFactors import prime_factors_of


class Test(TestCase):
    def test_prime_factors_of_1(self):
        n = 1

        expected = []
        self.assertEqual(expected, prime_factors_of(n))

    def test_prime_factors_of_2(self):
        n = 2

        expected = [2]
        self.assertEqual(expected, prime_factors_of(n))

    def test_prime_factors_of_3(self):
        n = 3

        expected = [3]
        self.assertEqual(expected, prime_factors_of(n))
