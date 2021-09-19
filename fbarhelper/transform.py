import os
import pandas


def main():
    df = pandas.read_csv('C:/code/python3/fbarhelper/tests/testdata/Transactions_1.csv',
                         sep=';',
                         encoding='ISO-8859-1',
                         parse_dates=['Buchungstag']
                         )
    print(df[['Buchungstag', 'Verwendungszweck', 'Soll', 'Waehrung']])

if __name__ == '__main__':
    main()
