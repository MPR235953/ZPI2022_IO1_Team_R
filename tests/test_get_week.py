import unittest
from unittest.mock import patch
from src.main import get_week


class MyTestCase(unittest.TestCase):
    @patch('src.main.get_date', return_value='2023-05-02')
    @patch('src.main.get_today', return_value='2023-05-09')
    @patch('src.main.requests.get')
    @patch('src.main.extract_data', return_value=[4.1823, 4.1547, 4.1612, 4.1384, 4.1609])
    def test_get_week(self, mock_extract_data, mock_get, mock_get_today, mock_get_date):

        code = 'USD'

        # Call the function
        actual_data = get_week(code)

        # Check that the expected URL was constructed
        expected_url = 'http://api.nbp.pl/api/exchangerates/rates/A/USD/2023-05-02/2023-05-09/'
        mock_get.assert_called_once_with(expected_url)

        # Check that the response was processed correctly
        mock_extract_data.assert_called_once_with(mock_get.return_value.json())

        # Check the result
        expected_data = [4.1823, 4.1547, 4.1612, 4.1384, 4.1609]
        self.assertEqual(actual_data, expected_data)


if __name__ == '__main__':
    unittest.main()
