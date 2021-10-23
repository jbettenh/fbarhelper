import csv
import sqlite3

import pandas


def import_bank_csv(csv_file):

    df = pandas.read_csv(csv_file,
                         sep=';',
                         encoding='ISO-8859-1',
                         quoting=csv.QUOTE_NONE
                         #dtype={'Soll': 'float64'}
                         )
    data = df.replace('"', '', regex=True)

    # Convert from dd.mm.yyyy to yyyy-mm-dd
    data['Buchungstag'] = pandas.to_datetime(data['Buchungstag'], format='%d.%m.%Y').dt.date
    data['Wert'] = pandas.to_datetime(data['Wert'], format='%d.%m.%Y').dt.date
    data['Soll'].astype('float')
    return data


def import_bank_data_to_db(bank_data):
    bank_data.to_sql(name='transactions',
                     con=sqlite3.connect('fbar.db'),
                     if_exists='replace',
                     index=True)


if __name__ == '__main__':
    db = import_bank_csv('C:/code/python3/fbarhelper/tests/testdata/Transactions_999_123456789_20210622_092547.csv')
    import_bank_data_to_db(db)

