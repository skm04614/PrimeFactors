from unittest import TestCase

from PrimeFactors import prime_factors_of


class Test(TestCase):
    def test_prime_factors_of_1(self):
        n = 1

        expected = [1]
        self.assertEqual(expected, prime_factors_of(n))
