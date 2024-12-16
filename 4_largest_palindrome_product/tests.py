import unittest
from main import largest_palindrome_product

class MyTestCase(unittest.TestCase):
    def test_returns_number(self):
        result = largest_palindrome_product(2)
        # Ensure booleans are not considered a valid return type
        self.assertTrue(isinstance(result, (int, float)) and not isinstance(result, bool),
                        "Return value should be a number")

    def test_largestPalindromeProduct_2(self):
        self.assertEqual(largest_palindrome_product(2), 9009)

    def test_largestPalindromeProduct_3(self):
        self.assertEqual(largest_palindrome_product(3), 906609)


if __name__ == '__main__':
    unittest.main()
