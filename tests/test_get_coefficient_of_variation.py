import unittest
from src.main import get_coefficient_of_variation


class MyTestCase(unittest.TestCase):
    def test_get_coefficient_of_variation_single_value(self):
        data = [5]
        expected_result = 0.0
        result = get_coefficient_of_variation(data)
        self.assertEqual(result, expected_result)

    def test_get_coefficient_of_variation_multiple_values(self):
        data = [1, 2, 3, 4, 5]
        expected_result = 0.47140452
        result = get_coefficient_of_variation(data)
        self.assertAlmostEqual(result, expected_result, places=8)


if __name__ == '__main__':
    unittest.main()
