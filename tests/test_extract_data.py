import unittest
from src.main import extract_data


class MyTestCase(unittest.TestCase):
    def test_extract_data(self):
        json = {
            'rates': [
                {'mid': 3.5},
                {'mid': 4.2},
                {'mid': 4.8},
                {'mid': 5.1},
                {'mid': 5.5},
            ]
        }
        expected_data = [3.5, 4.2, 4.8, 5.1, 5.5]

        # test func
        actual_data = extract_data(json)

        # test res
        self.assertEqual(actual_data, expected_data)


if __name__ == '__main__':
    unittest.main()
