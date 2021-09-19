import os
import pandas


def main():
    df = pandas.read_csv('C:/code/python3/fbarhelper/tests/testdata/Transactions_2.csv', delimiter=',')
    print(df)


if __name__ == '__main__':
    main()
