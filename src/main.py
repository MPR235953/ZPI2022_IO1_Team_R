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


def get_two_week(code):
    url = 'http://api.nbp.pl/api/exchangerates/rates/A/' + code + '/' + get_date(14) + '/' + get_today() + '/'
    response = requests.get(url)
    data = extract_data(response.json())
    return data


def get_month(code):
    url = 'http://api.nbp.pl/api/exchangerates/rates/A/' + code + '/' + get_date(31) + '/' + get_today() + '/'
    response = requests.get(url)
    data = extract_data(response.json())
    return data


def get_quarter(code):
    url = 'http://api.nbp.pl/api/exchangerates/rates/A/' + code + '/' + get_date(93) + '/' + get_today() + '/'
    response = requests.get(url)
    data = extract_data(response.json())
    return data


def get_half_year(code):
    url = 'http://api.nbp.pl/api/exchangerates/rates/A/' + code + '/' + get_date(93) + '/' + get_today() + '/'
    url2 = 'http://api.nbp.pl/api/exchangerates/rates/A/' + code + '/' + get_date(186) + '/' + get_date(93) + '/'
    response = requests.get(url)
    response2 = requests.get(url2)
    data1 = extract_data(response.json())
    data2 = extract_data(response2.json())
    return data1 + data2


if __name__ == '__main__':
    pass
