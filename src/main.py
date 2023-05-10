import datetime
import requests
import numpy as np


USD_CODE = 'USD'
EUR_CODE = 'EUR'


def get_today():
    return datetime.datetime.today().strftime('%Y-%m-%d')


def get_date(offset):
    date = datetime.datetime.today() - datetime.timedelta(days=offset)
    return date.strftime('%Y-%m-%d')


def extract_data(json):
    try:
        rates = json['rates']
        data = []
        for rate in rates:
            data.append(rate['mid'])
        return data
    except Exception:
        return None


def get_week(code):
    url = 'http://api.nbp.pl/api/exchangerates/rates/A/' + code + '/' + get_date(7) + '/' + get_today() + '/'
    response = requests.get(url)
    if response.status_code == 200:
        data = extract_data(response.json())
        return data
    else:
        return None


def get_two_week(code):
    url = 'http://api.nbp.pl/api/exchangerates/rates/A/' + code + '/' + get_date(14) + '/' + get_today() + '/'
    response = requests.get(url)
    if response.status_code == 200:
        data = extract_data(response.json())
        return data
    else:
        return None


def get_month(code):
    url = 'http://api.nbp.pl/api/exchangerates/rates/A/' + code + '/' + get_date(31) + '/' + get_today() + '/'
    response = requests.get(url)
    if response.status_code == 200:
        data = extract_data(response.json())
        return data
    else:
        return None


def get_quarter(code):
    url = 'http://api.nbp.pl/api/exchangerates/rates/A/' + code + '/' + get_date(93) + '/' + get_today() + '/'
    response = requests.get(url)
    if response.status_code == 200:
        data = extract_data(response.json())
        return data
    else:
        return None


def get_half_year(code):
    url = 'http://api.nbp.pl/api/exchangerates/rates/A/' + code + '/' + get_date(93) + '/' + get_today() + '/'
    url2 = 'http://api.nbp.pl/api/exchangerates/rates/A/' + code + '/' + get_date(186) + '/' + get_date(93) + '/'
    response = requests.get(url)
    response2 = requests.get(url2)
    if response.status_code == 200 and response2.status_code == 200:
        data1 = extract_data(response.json())
        data2 = extract_data(response2.json())
        return data1 + data2
    else:
        return None


def get_year(code):
    url = 'http://api.nbp.pl/api/exchangerates/rates/A/' + code + '/' + get_date(93) + '/' + get_today() + '/'
    url2 = 'http://api.nbp.pl/api/exchangerates/rates/A/' + code + '/' + get_date(186) + '/' + get_date(93) + '/'
    url3 = 'http://api.nbp.pl/api/exchangerates/rates/A/' + code + '/' + get_date(279) + '/' + get_date(186) + '/'
    url4 = 'http://api.nbp.pl/api/exchangerates/rates/A/' + code + '/' + get_date(372) + '/' + get_date(279) + '/'
    response = requests.get(url)
    response2 = requests.get(url2)
    response3 = requests.get(url3)
    response4 = requests.get(url4)
    if response.status_code == 200 and response2.status_code == 200 and response3.status_code == 200 and response4.status_code == 200:
        data1 = extract_data(response.json())
        data2 = extract_data(response2.json())
        data3 = extract_data(response3.json())
        data4 = extract_data(response4.json())
        return data1 + data2 + data3 + data4
    else:
        return None


def get_median(data):
    try:
        data = np.sort(data)
        median = np.median(data)
        return median
    except Exception:
        return None


if __name__ == '__main__':
    pass
