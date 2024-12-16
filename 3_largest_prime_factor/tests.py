import unittest
from main import largest_prime_factor

class MyTestCase(unittest.TestCase):
    def test_returns_number(self):
        result = largest_prime_factor(2)
        # Ensure booleans are not considered a valid return type
        self.assertTrue(isinstance(result, (int, float)) and not isinstance(result, bool),
                        "Return value should be a number")

    def test_largestPrimeFactor_2(self):
        self.assertEqual(largest_prime_factor(2), 2)

    def test_largestPrimeFactor_3(self):
        self.assertEqual(largest_prime_factor(3), 3)

    def test_largestPrimeFactor_5(self):
        self.assertEqual(largest_prime_factor(5), 5)

    def test_largestPrimeFactor_7(self):
        self.assertEqual(largest_prime_factor(7), 7)

    def test_largestPrimeFactor_8(self):
        self.assertEqual(largest_prime_factor(8), 2)

    def test_largestPrimeFactor_13195(self):
        self.assertEqual(largest_prime_factor(13195), 29)

    def test_largestPrimeFactor_600851475143(self):
        self.assertEqual(largest_prime_factor(600851475143), 6857)


if __name__ == '__main__':
    unittest.main()
