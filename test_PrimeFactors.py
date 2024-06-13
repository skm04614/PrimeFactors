from unittest import TestCase

from PrimeFactors import prime_factors_of


class Test(TestCase):
    def test_prime_factors_of_n(self):
        n_to_expected = {
            1: [],
            2: [2],
            3: [3],
            4: [2, 2],
            6: [2, 3],
            9: [3, 3],
            11: [11],
            13: [13],
            19: [19],
            20: [2, 2, 5],
            60: [2, 2, 3, 5]
        }

        for n, expected in n_to_expected.items():
            self.assertEqual(expected, prime_factors_of(n))
