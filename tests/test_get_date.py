import unittest
import datetime
from src.main import get_date


class MyTestCase(unittest.TestCase):
    def test_offset_zero(self):
        expected_date = datetime.datetime.today().strftime('%Y-%m-%d')
        self.assertEqual(get_date(0), expected_date)

    def test_offset_one(self):
        expected_date = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        self.assertEqual(get_date(1), expected_date)

    def test_offset_seven(self):
        expected_date = (datetime.datetime.today() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
        self.assertEqual(get_date(7), expected_date)

    def test_offset_year(self):
        expected_date = (datetime.datetime.today() - datetime.timedelta(days=365)).strftime('%Y-%m-%d')
        self.assertEqual(get_date(365), expected_date)


if __name__ == '__main__':
    unittest.main()

