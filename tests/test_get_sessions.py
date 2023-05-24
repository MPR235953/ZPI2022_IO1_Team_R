import unittest
from src.main import get_sessions


class MyTestCase(unittest.TestCase):
    def test_get_sessions_empty_list(self):
        data = []
        expected_result = [0, 0, 0]
        result = get_sessions(data)
        self.assertEqual(result, expected_result)

    def test_get_sessions_single_session_increasing(self):
        data = [1, 2, 3, 4, 5]
        expected_result = [0, 0, 1]
        result = get_sessions(data)
        self.assertEqual(result, expected_result)

    def test_get_sessions_single_session_decreasing(self):
        data = [5, 4, 3, 2, 1]
        expected_result = [1, 0, 0]
        result = get_sessions(data)
        self.assertEqual(result, expected_result)

    def test_get_sessions_single_session_zero(self):
        data = [1, 1, 1, 1, 1]
        expected_result = [0, 1, 0]
        result = get_sessions(data)
        self.assertEqual(result, expected_result)

    def test_get_sessions_multiple_sessions(self):
        data = [1, 2, 3, 4, 4, 4, 5, 4, 3, 2]
        expected_result = [1, 1, 2]
        result = get_sessions(data)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
