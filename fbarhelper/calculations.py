import locale
import sqlite3


def get_max_credit():
    conn = sqlite3.connect('fbar.db')

    with conn:
        c = conn.cursor()
        c.execute("SELECT MAX(AMOUNT), BOOKING_DATE FROM TRANSACTIONS;")
        print(f'Largest credit was: {c.fetchone()}')


def get_max_debit():
    conn = sqlite3.connect('fbar.db')

    with conn:
        c = conn.cursor()
        c.execute("SELECT MIN(AMOUNT), BOOKING_DATE FROM TRANSACTIONS;")
        row = c.fetchone()
        value = locale.currency(row['MIN(AMOUNT)'], grouping=True)
        print(f'Largest debit was: {value}')


if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, '')
    get_max_credit()
    get_max_debit()