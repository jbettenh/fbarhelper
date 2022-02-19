import locale
import sqlite3


def input_balance(date, amount):
    output = ''
    # Add more validation
    amount = float(amount.replace('.', ''))

    conn = sqlite3.connect('fbar.db')
    with conn:
        conn.execute("INSERT INTO TRANSACTIONS (BOOKING_DATE, DATE, BALANCE, CURRENCY) "
                     "VALUES (?, ?, ?, 'EUR')", (date, date, amount))

        output = 'Successful'
    return output
        

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

