import csv
import os
import pandas


def main():

    df = pandas.read_csv('C:/code/python3/fbarhelper/tests/testdata/Transactions_999_123456789_20210622_092547.csv',
                         sep=';',
                         encoding='ISO-8859-1',
                         parse_dates=['Buchungstag'],
                         quoting=csv.QUOTE_NONE
                         )
    data = df.replace('"', '', regex=True)
    print(data[['Buchungstag', 'Verwendungszweck', 'Soll', 'Haben']])


if __name__ == '__main__':
    main()
