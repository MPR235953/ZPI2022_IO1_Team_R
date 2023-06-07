import datetime
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
        today = datetime.datetime.today().strftime('%Y-%m-%d')
        days_back = (datetime.datetime.today() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
        mock_get.assert_called_once_with(
            'http://api.nbp.pl/api/exchangerates/rates/A/EUR/{days_back}/{today}/'.format(days_back=days_back, today=today))


if __name__ == '__main__':
    unittest.main()
