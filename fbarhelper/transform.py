import csv
import os
import sqlite3

import numpy as np
import pandas
import pandas as pd


def main(indir, outdir):

    li = []

    for root, dirs, filenames in os.walk(indir):
        for f in filenames:
            raw_filename = os.path.join(root, f)
            cleaned_filename = os.path.join(outdir, 'cleaned_' + f)
            if '.csv' in raw_filename:
                csv_cleaner(raw_filename, cleaned_filename)

    for root, dirs, filenames in os.walk(outdir):
        for filename in filenames:
            filepath = os.path.join(root, filename)
            df = import_bank_csv(filepath)
            li.append(df)

    frame = pd.concat(li, axis=0, ignore_index=True)
    import_bank_data_to_db(frame)


def csv_cleaner(raw_file, cleaned_file, header_rows=3, footer_rows=1, ):
    """
    Take the raw csv export from Deutsche Bank and create a csv of just transactions.
    """
    print(f'Cleaning CSV files in {raw_file} .....')
    try:
        with open(raw_file, 'r', encoding='ISO-8859-1') as fin, \
                open(cleaned_file, 'w', encoding='ISO-8859-1', newline='') as fout:

            file = csv.reader(fin, delimiter=';', lineterminator='\n')
            writer = csv.writer(fout, delimiter=';')

            for current_row, line in enumerate(file):
                if current_row > header_rows and "Account balance" not in line:
                    writer.writerow(line)

    except IOError as err:
        print(f"IOError {err} in ", raw_file)


def import_bank_csv(csv_file):

    print(f'Importing bank csv {csv_file} .....')
    df = pandas.read_csv(csv_file,
                         sep=';',
                         encoding='ISO-8859-1',
                         quoting=csv.QUOTE_NONE,
                         index_col=None
                         )
    df = df.replace('"', '', regex=True)
    df.columns = ['BOOKING_DATE', 'DATE', 'TRANSACTION_TYPE', 'RECIPIENT', 'USAGE', 'IBAN', 'BIC', 'CUSTOMER_REF',
                  'MANDATE_REF', 'CREDITOR_ID', 'FOREIGN_FEES', 'SUM', 'ALTERNATIVE_RECIPIENT', 'NO_ORDERS',
                  'NO_CHECKS', 'DEBIT', 'CREDIT', 'CURRENCY']
        
    df['BOOKING_DATE'] = pandas.to_datetime(df['BOOKING_DATE'], format='%d/%m/%Y').dt.date
    df['DATE'] = pandas.to_datetime(df['DATE'], format='%d/%m/%Y').dt.date
    df['CREDIT'] = pandas.to_numeric(df['CREDIT'].replace('[^0-9\-]', '', regex=True)).fillna(0)
    df['DEBIT'] = pandas.to_numeric(df['DEBIT'].replace('[^0-9\.-]', '', regex=True)).fillna(0)

    df['CREDIT'] = (df['CREDIT'].astype('float')).astype(int)
    df['DEBIT'] = (df['DEBIT'].astype('float')).astype(int)

    df['AMOUNT'] = df['CREDIT'] + df['DEBIT']
    df['BALANCE'] = np.NAN

    return df


def add_day_balance():
    conn = sqlite3.connect('fbar.db')

    with conn:
        conn.execute("INSERT INTO TRANSACTIONS (BOOKING_DATE, DATE, BALANCE, CURRENCY) "
                     "VALUES ('2021-01-01', '2021-01-01', 100000, 'EUR')")
        conn.execute("INSERT INTO TRANSACTIONS (BOOKING_DATE, DATE, BALANCE, CURRENCY) "
                     "VALUES ('2021-02-01', '2021-02-01', 173506, 'EUR')")


def import_bank_data_to_db(bank_data):
    print('Adding to database .....')
    bank_data.to_sql(name='TRANSACTIONS',
                     con=sqlite3.connect('fbar.db'),
                     if_exists='append',
                     index=True,
                     index_label='ID')


if __name__ == '__main__':

    main('C:/code/python3/fbarhelper/tests/testdata/', 'C:/code/python3/fbarhelper/cleaned_files/')
    add_day_balance()
    print('Inserted balances')
