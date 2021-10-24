import csv
import sqlite3

import pandas


def csv_cleaner(csv_file):
    pass


def import_bank_csv(csv_file):

    df = pandas.read_csv(csv_file,
                         sep=';',
                         encoding='ISO-8859-1',
                         quoting=csv.QUOTE_NONE
                         #dtype={'Soll': 'float64'}
                         )
    df = df.replace('"', '', regex=True)
    df.columns = ['BOOKING_DATE', 'DATE', 'TRANSACTION_TYPE', 'AUFTRAGGABER', 'USAGE', 'IBAN', 'BIC', 'CUSTUMER_REF',
                  'MANDATE_REF', 'CREDITOR_ID', 'FOREIGN_FEES', 'SUM', 'RECEIVER', 'NO_ORDERS', 'NO_CHECKS',
                  'DEBIT', 'CREDIT', 'CURRENCY']
        
    # Convert from dd.mm.yyyy to yyyy-mm-dd
    df['BOOKING_DATE'] = pandas.to_datetime(df['BOOKING_DATE'], format='%d.%m.%Y').dt.date
    df['DATE'] = pandas.to_datetime(df['DATE'], format='%d.%m.%Y').dt.date
    # data['DEBIT'].astype('float')
    # data['CREDIT'].astype('float')

    return df


def import_bank_data_to_db(bank_data):
    bank_data.to_sql(name='transactions',
                     con=sqlite3.connect('fbar.db'),
                     if_exists='replace',
                     index=True)


if __name__ == '__main__':
    db = import_bank_csv('C:/code/python3/fbarhelper/tests/testdata/Transactions_999_123456789_20210622_092547.csv')
    import_bank_data_to_db(db)

