import sqlite3


def create_tables():
    conn = sqlite3.connect('fbar.db')

    with conn:
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS
               translations(ID INTEGER PRIMARY KEY, DE TEXT, EN TEXT, DESCRIPTION TEXT)""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS
                   transactions(ID INTEGER PRIMARY KEY not null on conflict ignore, BOOKING_DATE DATE, DATE DATE, 
                   TRANSACTION_TYPE TEXT, RECIPIENT TEXT, USAGE TEXT, IBAN TEXT, BIC TEXT, CUSTOMER_REF TEXT, 
                   MANDATE_REF TEXT,CREDITOR_ID TEXT, FOREIGN_FEES TEXT, SUM REAL, ALTERNATIVE_RECIPIENT TEXT, 
                   NO_ORDERS TEXT, NO_CHECKS TEXT, DEBIT REAL, CREDIT REAL, CURRENCY TEXT)""")


def translate_column_names():
    conn = sqlite3.connect('fbar.db')

    with conn:
        conn.execute("INSERT INTO translations VALUES ('0', 'Buchungstag', 'Booking Date', "
                       "'Date Deutsche Bank recorded the transaction' )")
        conn.execute("INSERT INTO translations VALUES ('1', 'Wert', 'Date', "
                       "'Date Deutsche Bank recorded the transaction' )")
        conn.execute("INSERT INTO translations VALUES ('2', 'Umsatzart', 'Transaction Type', '' )")
        conn.execute("INSERT INTO translations VALUES ('3', 'Begünstigter / Auftraggaber', 'Recipient', '' )")
        conn.execute("INSERT INTO translations VALUES ('4', 'Verwendungszweck', 'Usage','Intended purpose memo' )")
        conn.execute("INSERT INTO translations VALUES ('5', 'Kundenreferenz', 'Customer reference', '' )")
        conn.execute("INSERT INTO translations VALUES ('6', 'Mandatsreferenz', 'Mandate reference', '' )")
        conn.execute("INSERT INTO translations VALUES ('7', 'Gläubiger ID', 'Creditor identifier', '' )")
        conn.execute("INSERT INTO translations VALUES ('8', 'Fremde Gebühren', 'Foreign fees', '' )")
        conn.execute("INSERT INTO translations VALUES ('9', 'Betrag', 'Sum', '' )")
        conn.execute("INSERT INTO translations VALUES ('10', 'Abweichender Empfänger', 'Alternative Recipient', '' )")
        conn.execute("INSERT INTO translations VALUES ('11', 'Anzahl der Aufträge', 'No of orders', '' )")
        conn.execute("INSERT INTO translations VALUES ('12', 'Anzahl der Schecks', 'No of checks', '' )")
        conn.execute("INSERT INTO translations VALUES ('13', 'Soll', 'Debit', '' )")
        conn.execute("INSERT INTO translations VALUES ('14', 'Haben', 'Credit', '' )")
        conn.execute("INSERT INTO translations VALUES ('15', 'Währung', 'Currency', '' )")


if __name__ == '__main__':
    create_tables()
    translate_column_names()