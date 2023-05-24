import unittest
from unittest import mock
from src.main import get_week


class MyTestCase(unittest.TestCase):

    @mock.patch('requests.get')
    def test_get_week_failed_request(self, mock_get):
        code = 'EUR'
        mock_response = mock.Mock()
        mock_response.ok = False
        mock_get.return_value = mock_response

        result = get_week(code)

        self.assertIsNone(result)
        mock_get.assert_called_once_with(
            'http://api.nbp.pl/api/exchangerates/rates/A/EUR/2023-05-17/2023-05-24/')


if __name__ == '__main__':
    unittest.main()
