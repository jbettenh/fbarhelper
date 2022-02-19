import locale
import sqlite3
import datetime


def input_balance(booking_date, date, amount):
    locale.setlocale(locale.LC_ALL, 'en_US')
    date_format = '%Y-%m-%d'
    # Add more validation
    try:
        datetime.datetime.strptime(booking_date, date_format)
        datetime.datetime.strptime(date, date_format)
    except ValueError:
        print('This is the incorrect date format. It should be YYYY-MM-DD')
        return False

    except:
        print('Unknown error with date entered.')
        return False


    try:
        amount = (locale.atof(amount))*100
    except ValueError:
        print('Float error')
        return False
    except:
        print('Unknown error with amount entered.')
        return False

    conn = sqlite3.connect('fbar.db')

    with conn:
        conn.execute("INSERT INTO TRANSACTIONS (BOOKING_DATE, DATE, BALANCE, CURRENCY) "
                     "VALUES (?, ?, ?, 'EUR')", (booking_date, date, amount))
        print('Successful')
    return True
        

def calc_daily_balance():
    pass


def get_max_credit():
    locale.setlocale(locale.LC_ALL, 'de_DE')
    conn = sqlite3.connect('fbar.db')

    with conn:
        c = conn.cursor()
        c.execute("SELECT MAX(AMOUNT), BOOKING_DATE FROM TRANSACTIONS;")
        data = c.fetchone()

        if data is not None:
            amount, date = data
            amount = locale.currency(amount/100)
            return amount, date


def get_max_debit():
    locale.setlocale(locale.LC_ALL, 'de_DE')
    conn = sqlite3.connect('fbar.db')

    with conn:
        c = conn.cursor()
        c.execute("SELECT MIN(AMOUNT), BOOKING_DATE FROM TRANSACTIONS;")
        data = c.fetchone()

        if data is not None:
            amount, date = data
            amount = locale.currency(amount / 100)
            return amount, date


def get_max_balance():
    locale.setlocale(locale.LC_ALL, 'de_DE')
    conn = sqlite3.connect('fbar.db')

    with conn:
        c = conn.cursor()
        c.execute("SELECT MAX(BALANCE), BOOKING_DATE FROM TRANSACTIONS")
        data = c.fetchone()

        if data is not None:
            balance, date = data
            balance = locale.currency(balance / 100)
            return balance, date


if __name__ == '__main__':
    print(f'Largest credit was: {get_max_credit()[0]} on {get_max_credit()[1]}')
    print(f'Largest debit was: {get_max_debit()[0]} on {get_max_debit()[1]}')
    print(f'Largest balance was: {get_max_balance()[0]} on {get_max_balance()[1]}')

