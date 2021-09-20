import csv
import os
import pandas


def main():

    df = pandas.read_csv('C:/code/python3/fbarhelper/tests/testdata/Transactions_3.csv',
                         sep=';',
                         encoding='ISO-8859-1',
                         parse_dates=['Buchungstag'],
                         quoting=csv.QUOTE_NONE
                         )
    print(df[['Buchungstag', 'Verwendungszweck', 'Soll']])


if __name__ == '__main__':
    main()
