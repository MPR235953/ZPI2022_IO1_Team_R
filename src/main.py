import datetime
import requests

USD_CODE = 'USD'
EUR_CODE = 'EUR'


def get_today():
    return datetime.datetime.today().strftime('%Y-%m-%d')


def get_date(offset):
    date = datetime.datetime.today() - datetime.timedelta(days=offset)
    return date.strftime('%Y-%m-%d')


def extract_data(json):
    rates = json['rates']
    data = []
    for rate in rates:
        data.append(rate['mid'])
    return data


def get_week(code):
    url = 'http://api.nbp.pl/api/exchangerates/rates/A/' + code + '/' + get_date(7) + '/' + get_today() + '/'
    response = requests.get(url)
    data = extract_data(response.json())
    return data


def get_month(code):
    url = 'http://api.nbp.pl/api/exchangerates/rates/A/' + code + '/' + get_date(31) + '/' + get_today() + '/'
    response = requests.get(url)
    data = extract_data(response.json())
    return data


if __name__ == '__main__':
    pass
