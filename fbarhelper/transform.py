import os
import pandas


def main():
    df = pandas.read_csv('C:/code/python3/fbarhelper/tests/testdata/Transactions_999_123456789_20210622_092547.csv', delimiter=';', encoding='ISO-8859-1')
    print(df)


if __name__ == '__main__':
    main()
