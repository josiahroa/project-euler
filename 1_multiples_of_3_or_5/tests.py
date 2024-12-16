import unittest
from main import multiples_of_3_or_5

class MyTestCase(unittest.TestCase):
    def test_return_type(self):
        result = multiples_of_3_or_5(10)
        # Ensure booleans are not considered a valid return type
        self.assertTrue(isinstance(result, (int, float)) and not isinstance(result, bool),
                        "Return value should be a number")

    def test_case_49(self):
        self.assertEqual(multiples_of_3_or_5(49), 543)

    def test_case_1000(self):
        self.assertEqual(multiples_of_3_or_5(1000), 233168)

    def test_case_8456(self):
        self.assertEqual(multiples_of_3_or_5(8456), 16687353)

    def test_case_19564(self):
        self.assertEqual(multiples_of_3_or_5(19564), 89301183)


if __name__ == '__main__':
    unittest.main()
