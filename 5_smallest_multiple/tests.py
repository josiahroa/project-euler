import unittest
from main import smallest_multiple

class MyTestCase(unittest.TestCase):
    def test_returns_number(self):
        result = smallest_multiple(5)
        # Ensure booleans are not considered a valid return type
        self.assertTrue(isinstance(result, (int, float)) and not isinstance(result, bool),
                        "Return value should be a number")

    def test_smallestMult_5(self):
        self.assertEqual(smallest_multiple(5), 60)

    def test_smallestMult_7(self):
        self.assertEqual(smallest_multiple(7), 420)

    def test_smallestMult_10(self):
        self.assertEqual(smallest_multiple(10), 2520)

    def test_smallestMult_13(self):
        self.assertEqual(smallest_multiple(13), 360360)

    def test_smallestMult_20(self):
        self.assertEqual(smallest_multiple(20), 232792560)


if __name__ == '__main__':
    unittest.main()
