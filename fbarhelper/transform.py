import csv
import sqlite3

import pandas


def main():

    df = pandas.read_csv('C:/code/python3/fbarhelper/tests/testdata/Transactions_999_123456789_20210622_092547.csv',
                         sep=';',
                         encoding='ISO-8859-1',
                         parse_dates=['Buchungstag'],
                         quoting=csv.QUOTE_NONE
                         )
    data = df.replace('"', '', regex=True)

    data.to_sql(name='transactions',
                con=sqlite3.connect('fbar.db'),
                if_exists='replace',
                index=True)


if __name__ == '__main__':

    main()

