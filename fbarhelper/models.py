import sqlite3


def drop_tables():
    conn = sqlite3.connect('fbar.db')

    with conn:
        cursor = conn.cursor()
        cursor.execute("DROP TABLE TRANSLATIONS")
        cursor.execute("DROP TABLE TRANSACTIONS")
        cursor.execute("DROP TABLE ACCOUNTS")
        cursor.execute("DROP TABLE BANKS")


def insert_tables():
    conn = sqlite3.connect('fbar.db')

    with conn:
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS
               TRANSLATIONS(ID INTEGER PRIMARY KEY, DE TEXT, EN TEXT, DESCRIPTION TEXT)""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS
                   TRANSACTIONS(ID INTEGER PRIMARY KEY not null on conflict ignore, BOOKING_DATE DATE, DATE DATE, 
                   TRANSACTION_TYPE TEXT, RECIPIENT TEXT, USAGE TEXT, IBAN TEXT, BIC TEXT, CUSTOMER_REF TEXT, 
                   MANDATE_REF TEXT,CREDITOR_ID TEXT, FOREIGN_FEES TEXT, SUM REAL, ALTERNATIVE_RECIPIENT TEXT, 
                   NO_ORDERS TEXT, NO_CHECKS TEXT, DEBIT INTEGER, CREDIT INTEGER, AMOUNT INTEGER, BALANCE INTEGER,
                   CURRENCY TEXT)""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS
                           ACCOUNTS(ID INTEGER PRIMARY KEY not null on conflict ignore, NAME TEXT, OWNER_FIRST TEXT,
                           OWNER_LAST TEXT, ACCOUNT_NO TEXT, IBAN TEXT, BIC TEXT, DATE_OPENED DATE, ACCOUNT_TYPE TEXT, 
                           CURRENT_BALANCE INTEGER)""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS
                                   BANKS(ID INTEGER PRIMARY KEY not null on conflict ignore, NAME TEXT, 
                                   ADDRESS TEXT)""")


def translate_column_names():
    conn = sqlite3.connect('fbar.db')

    with conn:
        conn.execute("INSERT INTO TRANSLATIONS VALUES ('0', 'Buchungstag', 'Booking Date',"
                     "'Date Deutsche Bank recorded the transaction' )")
        conn.execute("INSERT INTO TRANSLATIONS VALUES ('1', 'Wert', 'Date',"
                     "'Date Deutsche Bank recorded the transaction' )")
        conn.execute("INSERT INTO TRANSLATIONS VALUES ('2', 'Umsatzart', 'Transaction Type', '' )")
        conn.execute("INSERT INTO TRANSLATIONS VALUES ('3', 'Begünstigter / Auftraggaber', 'Recipient', '' )")
        conn.execute("INSERT INTO TRANSLATIONS VALUES ('4', 'Verwendungszweck', 'Usage','Intended purpose memo' )")
        conn.execute("INSERT INTO TRANSLATIONS VALUES ('5', 'Kundenreferenz', 'Customer reference', '' )")
        conn.execute("INSERT INTO TRANSLATIONS VALUES ('6', 'Mandatsreferenz', 'Mandate reference', '' )")
        conn.execute("INSERT INTO TRANSLATIONS VALUES ('7', 'Gläubiger ID', 'Creditor identifier', '' )")
        conn.execute("INSERT INTO TRANSLATIONS VALUES ('8', 'Fremde Gebühren', 'Foreign fees', '' )")
        conn.execute("INSERT INTO TRANSLATIONS VALUES ('9', 'Betrag', 'Sum', '' )")
        conn.execute("INSERT INTO TRANSLATIONS VALUES ('10', 'Abweichender Empfänger', 'Alternative Recipient', '' )")
        conn.execute("INSERT INTO TRANSLATIONS VALUES ('11', 'Anzahl der Aufträge', 'No of orders', '' )")
        conn.execute("INSERT INTO TRANSLATIONS VALUES ('12', 'Anzahl der Schecks', 'No of checks', '' )")
        conn.execute("INSERT INTO TRANSLATIONS VALUES ('13', 'Soll', 'Debit', '' )")
        conn.execute("INSERT INTO TRANSLATIONS VALUES ('14', 'Haben', 'Credit', '' )")
        conn.execute("INSERT INTO TRANSLATIONS VALUES ('15', 'Währung', 'Currency', '' )")


if __name__ == '__main__':
    drop_tables()
    print('Tables dropped.')
    insert_tables()
    print('Tables inserted.')
    translate_column_names()
    print('Inserted header translations.')

