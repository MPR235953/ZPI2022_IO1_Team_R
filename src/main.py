import sys
import datetime
import threading
import requests
import numpy as np
import prettytable
import enum
import itertools

CODES = ["USD", "EUR"]
STATS = ["ses", "med", "std", "cov"]
global working


class Errors(enum.Enum):
    OK = 0
    UNSUPPORTED_COMMAND = 1
    NO_CONNECTION = 2


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
    except KeyError:
        return None


def get_week(code):
    try:
        url = 'http://api.nbp.pl/api/exchangerates/rates/A/' + code + '/' + get_date(7) + '/' + get_today() + '/'
        response = requests.get(url)
        if response.ok:
            data = extract_data(response.json())
            return data
        else:
            return None
    except requests.ConnectionError:
        return None

def get_two_week(code):
    try:
        url = 'http://api.nbp.pl/api/exchangerates/rates/A/' + code + '/' + get_date(14) + '/' + get_today() + '/'
        response = requests.get(url)
        if response.ok:
            data = extract_data(response.json())
            return data
        else:
            return None
    except requests.ConnectionError:
        return None

def get_month(code):
    try:
        url = 'http://api.nbp.pl/api/exchangerates/rates/A/' + code + '/' + get_date(31) + '/' + get_today() + '/'
        response = requests.get(url)
        if response.ok:
            data = extract_data(response.json())
            return data
        else:
            return None
    except requests.ConnectionError:
        return None

def get_quarter(code):
    try:
        url = 'http://api.nbp.pl/api/exchangerates/rates/A/' + code + '/' + get_date(93) + '/' + get_today() + '/'
        response = requests.get(url)
        if response.ok:
            data = extract_data(response.json())
            return data
        else:
            return None
    except requests.ConnectionError:
        return None

def get_half_year(code):
    try:
        url = 'http://api.nbp.pl/api/exchangerates/rates/A/' + code + '/' + get_date(93) + '/' + get_today() + '/'
        url2 = 'http://api.nbp.pl/api/exchangerates/rates/A/' + code + '/' + get_date(186) + '/' + get_date(93) + '/'
        response = requests.get(url)
        response2 = requests.get(url2)
        if response.ok and response2.ok:
            data1 = extract_data(response.json())
            data2 = extract_data(response2.json())
            return data1 + data2
        else:
            return None
    except requests.ConnectionError:
        return None


def get_year(code):
    try:
        url = 'http://api.nbp.pl/api/exchangerates/rates/A/' + code + '/' + get_date(93) + '/' + get_today() + '/'
        url2 = 'http://api.nbp.pl/api/exchangerates/rates/A/' + code + '/' + get_date(186) + '/' + get_date(93) + '/'
        url3 = 'http://api.nbp.pl/api/exchangerates/rates/A/' + code + '/' + get_date(279) + '/' + get_date(186) + '/'
        url4 = 'http://api.nbp.pl/api/exchangerates/rates/A/' + code + '/' + get_date(372) + '/' + get_date(279) + '/'
        response = requests.get(url)
        response2 = requests.get(url2)
        response3 = requests.get(url3)
        response4 = requests.get(url4)
        if response.ok and response2.ok and response3.ok and response4.ok:
            data1 = extract_data(response.json())
            data2 = extract_data(response2.json())
            data3 = extract_data(response3.json())
            data4 = extract_data(response4.json())
            return data1 + data2 + data3 + data4
        else:
            return None
    except requests.ConnectionError:
        return None


def process(lst):
    if lst.count(lst[0]) == len(lst):
        return [lst]

    if len(lst) < 2:
        return [lst]

    res = []
    temp = [lst[0]]
    is_up = lst[1] > lst[0]

    for i in range(1, len(lst)):
        curr = lst[i]
        prev = lst[i - 1]

        if (curr >= prev and not is_up) or (curr <= prev and is_up):
            res += [temp] + process(lst[i:])
            return res

        temp.append(curr)

    return [temp]


def get_sessions(data):
    try:
        data = process(data)
        increasing = 0
        decreasing = 0
        zero = 0
        for d in data:
            if (len(d) == 1) or d.count(d[0]) == len(d):
                zero += 1
            else:
                arr = np.array(d)
                diff = np.diff(arr)
                if np.all(diff > 0):
                    increasing += 1
                else:
                    decreasing += 1
        return [decreasing, zero, increasing]
    except IndexError:
        return None


def get_median(data):
    data = np.sort(data)
    median = np.median(data)
    return median


def get_standard_deviation(data):
    return np.std(data)


def get_coefficient_of_variation(data):
    return get_standard_deviation(data)/np.mean(data)


def get_all_data(code):
    week_data = get_week(code)
    two_week_data = get_two_week(code)
    month_data = get_month(code)
    quarter_data = get_quarter(code)
    half_year_data = get_half_year(code)
    year_data = get_year(code)
    if week_data is None or two_week_data is None or month_data is None or quarter_data is None or half_year_data is None or year_data is None:
        return None
    else:
        return [week_data, two_week_data, month_data, quarter_data, half_year_data, year_data]


def draw_sessions_table(data):
    try:
        x = prettytable.PrettyTable()
        x.field_names = ["period", "decreasing", "no changes", "increasing"]
        x.add_row(['one week'] + get_sessions(data[0]))
        x.add_row(['two weeks'] + get_sessions(data[1]))
        x.add_row(['one month'] + get_sessions(data[2]))
        x.add_row(['one quarter'] + get_sessions(data[3]))
        x.add_row(['half year'] + get_sessions(data[4]))
        x.add_row(['one year'] + get_sessions(data[5]))
        print(x)
    except IndexError:
        raise Exception("Not enough data")


def draw_med_table(data):
    try:
        x = prettytable.PrettyTable()
        x.field_names = ["period", "median"]
        x.add_row(['one week', get_median(data[0])])
        x.add_row(['two weeks', get_median(data[1])])
        x.add_row(['one month', get_median(data[2])])
        x.add_row(['one quarter', get_median(data[3])])
        x.add_row(['half year', get_median(data[4])])
        x.add_row(['one year', get_median(data[5])])
        print(x)
    except IndexError:
        raise Exception("Not enough data")


def draw_std_table(data):
    try:
        x = prettytable.PrettyTable()
        x.field_names = ["period", "standard deviation"]
        x.add_row(['one week', get_standard_deviation(data[0])])
        x.add_row(['two weeks', get_standard_deviation(data[1])])
        x.add_row(['one month', get_standard_deviation(data[2])])
        x.add_row(['one quarter', get_standard_deviation(data[3])])
        x.add_row(['half year', get_standard_deviation(data[4])])
        x.add_row(['one year', get_standard_deviation(data[5])])
        print(x)
    except IndexError:
        raise Exception("Not enough data")


def draw_cov_table(data):
    try:
        x = prettytable.PrettyTable()
        x.field_names = ["period", "coefficient of variation"]
        x.add_row(['one week', get_coefficient_of_variation(data[0])])
        x.add_row(['two weeks', get_coefficient_of_variation(data[1])])
        x.add_row(['one month', get_coefficient_of_variation(data[2])])
        x.add_row(['one quarter', get_coefficient_of_variation(data[3])])
        x.add_row(['half year', get_coefficient_of_variation(data[4])])
        x.add_row(['one year', get_coefficient_of_variation(data[5])])
        print(x)
    except IndexError:
        raise Exception("Not enough data")


def draw_table(stat, data):
    if stat == STATS[0]:
        draw_sessions_table(data)
    elif stat == STATS[1]:
        draw_med_table(data)
    elif stat == STATS[2]:
        draw_std_table(data)
    elif stat == STATS[3]:
        draw_cov_table(data)


def display_help():
    currencies = [["Code", "Name"], [CODES[0], "United States dollar"], [CODES[1], "Euro"]]
    commands = [["Command", "Description"],
                [STATS[0], "Displays increasing, decreasing and unchanging sessions for given currency data"],
                [STATS[1], "Displays median for given currency data"],
                [STATS[2], "Displays standard deviation for given currency data"],
                [STATS[3], "Displays coefficient of variation for given currency data"]]
    print("---------------------------------------------------------------------------------------------------")
    print("Supported currencies:")
    for entries in currencies:
        for entry in entries:
            print(entry.ljust(10), end='')
        print()
    print("\nSupported commands:")
    for entries in commands:
        for entry in entries:
            print(entry.ljust(10), end='')
        print()
    print("\nSample command usage:\nmain.py EUR med")
    print("\nDisplay help:\nmain.py help")
    print("---------------------------------------------------------------------------------------------------")


def handle_command(code, stat):
    global working
    working = True
    print("Downloading data...")
    spin_thread = threading.Thread(target=spin)
    spin_thread.start()
    if code in CODES and stat in STATS:
        data = get_all_data(code)
        working = False
        spin_thread.join()
        if data is None:
            return Errors.NO_CONNECTION
        else:
            print("Generating statistics...")
            draw_table(stat, data)
            print("Done.")
    else:
        working = False
        spin_thread.join()
        return Errors.UNSUPPORTED_COMMAND
    return Errors.OK


def spin():
    global working
    spinner = itertools.cycle(['-', '/', '|', '\\'])
    while working:
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        sys.stdout.write('\b')


if __name__ == '__main__':
    try:
        currency_code = sys.argv[1]
        if currency_code == "help":
            display_help()
            exit(0)
        statistic = sys.argv[2]
        return_code = handle_command(currency_code, statistic)

        if return_code is Errors.OK:
            input("Press Enter to exit...")
        elif return_code is Errors.NO_CONNECTION:
            print("Could not connect to API")
        elif return_code is Errors.UNSUPPORTED_COMMAND:
            print("Unsupported command or currency, see help")

    except IndexError:
        print("Not enough arguments provided")
