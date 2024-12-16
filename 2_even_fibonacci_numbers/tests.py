import unittest
from main import even_fibonacci_numbers

class MyTestCase(unittest.TestCase):
    def test_returns_number(self):
        result = even_fibonacci_numbers(10)
        self.assertTrue(isinstance(result, (int, float)) and not isinstance(result, bool),
                        "Return value should be a number")

    def test_returns_even_value(self):
        result = even_fibonacci_numbers(10)
        self.assertEqual(result % 2, 0)

    def test_fiboEvenSum_8(self):
        self.assertEqual(even_fibonacci_numbers(8), 10)

    def test_fiboEvenSum_10(self):
        self.assertEqual(even_fibonacci_numbers(10), 10)

    def test_fiboEvenSum_34(self):
        self.assertEqual(even_fibonacci_numbers(34), 44)

    def test_fiboEvenSum_60(self):
        self.assertEqual(even_fibonacci_numbers(60), 44)

    def test_fiboEvenSum_1000(self):
        self.assertEqual(even_fibonacci_numbers(1000), 798)

    def test_fiboEvenSum_100000(self):
        self.assertEqual(even_fibonacci_numbers(100000), 60696)

    def test_fiboEvenSum_4000000(self):
        self.assertEqual(even_fibonacci_numbers(4000000), 4613732)


if __name__ == '__main__':
    unittest.main()
