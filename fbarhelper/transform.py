import csv
import os
import sqlite3

import pandas


def main():
    # db = import_bank_csv('C:/code/python3/fbarhelper/tests/testdata/Transactions_1.csv')
    indir = 'C:/code/python3/fbarhelper/tests/testdata/'

    for root, dirs, filenames in os.walk(indir):
        for f in filenames:
            filename = os.path.join(root, f)
            if '.csv' in filename:
                csv_cleaner(filename, cleaned_file='cleaned_' +f)
    # import_bank_data_to_db(db)


def csv_cleaner(raw_file, cleaned_file, header_rows=3, footer_rows=1, ):
    """
    Take the raw csv export from Deutsche Bank and create a csv of just transactions.
    """

    try:
        with open(raw_file, 'r') as fin, open(cleaned_file, 'w') as fout:
            file = csv.reader(fin, delimiter=';', lineterminator='\n')
            writer = csv.writer(fout)
            for i, line in enumerate(file):
                if i > header_rows:
                    writer.writerow(line)

    except IOError as err:
        print(f"IOError {err} in ", raw_file)


def import_bank_csv(csv_file):

    df = pandas.read_csv(csv_file,
                         sep=';',
                         encoding='ISO-8859-1',
                         quoting=csv.QUOTE_NONE
                         )
    df = df.replace('"', '', regex=True)
    df.columns = ['BOOKING_DATE', 'DATE', 'TRANSACTION_TYPE', 'RECIPIENT', 'USAGE', 'IBAN', 'BIC', 'CUSTUMER_REF',
                  'MANDATE_REF', 'CREDITOR_ID', 'FOREIGN_FEES', 'SUM', 'ALTERNATIVE_RECIPIENT', 'NO_ORDERS',
                  'NO_CHECKS', 'DEBIT', 'CREDIT', 'CURRENCY']
        
    # Convert from dd.mm.yyyy to yyyy-mm-dd
    df['BOOKING_DATE'] = pandas.to_datetime(df['BOOKING_DATE'], format='%d.%m.%Y').dt.date
    df['DATE'] = pandas.to_datetime(df['DATE'], format='%d.%m.%Y').dt.date

    # Switch separators from German to US
    df['DEBIT'] = df['DEBIT'].str.replace('.', '')
    df['CREDIT'] = df['CREDIT'].str.replace('.', '')
    df['CURRENCY'] = df['CURRENCY'].str.replace(',', '')
    df['DEBIT'] = df['DEBIT'].str.replace(',', '.')
    df['CREDIT'] = df['CREDIT'].str.replace(',', '.')

    # Make values floats
    df['DEBIT'] = df['DEBIT'].astype('float')
    df['CREDIT'] = df['CREDIT'].astype('float')

    return df


def import_bank_data_to_db(bank_data):
    bank_data.to_sql(name='transactions',
                     con=sqlite3.connect('fbar.db'),
                     if_exists='replace',
                     index=True)


def get_max():
    conn = sqlite3.connect('fbar.db')
    c = conn.cursor()
    c.execute("SELECT MAX(CREDIT) FROM transactions;")

    print(c.fetchone())

    conn.close()


if __name__ == '__main__':
    main()
    get_max()

