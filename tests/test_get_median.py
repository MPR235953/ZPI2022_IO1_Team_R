import unittest
from src.main import get_median


class MyTestCase(unittest.TestCase):
    def test_get_median_odd_length(self):
        data = [5, 2, 9, 1, 7]
        expected_result = 5
        result = get_median(data)
        self.assertEqual(result, expected_result)

    def test_get_median_even_length(self):
        data = [4, 8, 1, 6]
        expected_result = 5.0
        result = get_median(data)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
