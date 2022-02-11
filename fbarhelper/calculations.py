import locale
import sqlite3


def get_max_credit():
    conn = sqlite3.connect('fbar.db')

    with conn:
        c = conn.cursor()
        c.execute("SELECT MAX(AMOUNT), BOOKING_DATE FROM TRANSACTIONS;")
        data = c.fetchone()

        if data is not None:
            balance, date = data
            balance = locale.currency(balance/100)
            return balance, date


def get_max_debit():
    conn = sqlite3.connect('fbar.db')

    with conn:
        c = conn.cursor()
        c.execute("SELECT MIN(AMOUNT), BOOKING_DATE FROM TRANSACTIONS;")
        data = c.fetchone()

        if data is not None:
            balance, date = data
            balance = locale.currency(balance / 100)
            return balance, date


if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, 'de_DE')
    print(f'Largest credit was: {get_max_credit()[0]} on {get_max_credit()[1]}')
    print(f'Largest debit was: {get_max_debit()[0]} on {get_max_debit()[1]}')
