import unittest
from unittest.mock import patch
from src.main import get_quarter


class MyTestCase(unittest.TestCase):
    @patch('src.main.get_date', return_value='2023-02-05')
    @patch('src.main.get_today', return_value='2023-05-09')
    @patch('src.main.requests.get')
    @patch('src.main.extract_data',
           return_value=[4.3833, 4.4325, 4.4074, 4.4003, 4.4565, 4.4856, 4.4463, 4.4372, 4.4601, 4.4888, 4.4515, 4.4524,
                         4.4687, 4.4873, 4.4630, 4.4697, 4.4475, 4.4094, 4.4002, 4.4341, 4.4289, 4.3981, 4.4626, 4.4356,
                         4.4266, 4.3906, 4.3793, 4.4030, 4.4248, 4.4202, 4.4130, 4.3715, 4.3467, 4.3011, 4.3742,
                         4.3518, 4.3300, 4.3247, 4.3043, 4.2934, 4.3168, 4.2855, 4.2739, 4.3033, 4.2932, 4.2917, 4.2713,
                         4.2225, 4.2042, 4.2261, 4.2151, 4.2244, 4.2024, 4.2006, 4.1905, 4.1649, 4.1557,
                         4.1541, 4.1753, 4.1823, 4.1547, 4.1612, 4.1384, 4.1609])
    def test_get_quarter(self, mock_extract_data, mock_get, mock_get_today, mock_get_date):
        code = 'USD'

        # Call the function
        actual_data = get_quarter(code)

        # Check that the expected URL was constructed
        expected_url = 'http://api.nbp.pl/api/exchangerates/rates/A/USD/2023-02-05/2023-05-09/'
        mock_get.assert_called_once_with(expected_url)

        # Check that the response was processed correctly
        mock_extract_data.assert_called_once_with(mock_get.return_value.json())

        # Check the result
        expected_data = [4.3833, 4.4325, 4.4074, 4.4003, 4.4565, 4.4856, 4.4463, 4.4372, 4.4601, 4.4888, 4.4515, 4.4524,
                         4.4687, 4.4873, 4.4630, 4.4697, 4.4475, 4.4094, 4.4002, 4.4341, 4.4289, 4.3981, 4.4626, 4.4356,
                         4.4266, 4.3906, 4.3793, 4.4030, 4.4248, 4.4202, 4.4130, 4.3715, 4.3467, 4.3011, 4.3742,
                         4.3518, 4.3300, 4.3247, 4.3043, 4.2934, 4.3168, 4.2855, 4.2739, 4.3033, 4.2932, 4.2917, 4.2713,
                         4.2225, 4.2042, 4.2261, 4.2151, 4.2244, 4.2024, 4.2006, 4.1905, 4.1649, 4.1557,
                         4.1541, 4.1753, 4.1823, 4.1547, 4.1612, 4.1384, 4.1609]
        self.assertEqual(actual_data, expected_data)


if __name__ == '__main__':
    unittest.main()
