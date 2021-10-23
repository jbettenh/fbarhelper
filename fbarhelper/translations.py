import sqlite3


def translate_column_names():
    conn = sqlite3.connect('fbar.db')

    cursor = conn.cursor()

    command1 = """CREATE TABLE IF NOT EXISTS
       translations(ID INTEGER PRIMARY KEY, DE TEXT, EN TEXT, DESCRIPTION TEXT)"""

    cursor.execute(command1)

    cursor.execute("INSERT INTO translations VALUES ('0', 'Buchungstag', 'Booking Date', "
                   "'Date Deutsche Bank recorded the transaction' )")
    cursor.execute("INSERT INTO translations VALUES ('1', 'Wert', 'Date', "
                   "'Date Deutsche Bank recorded the transaction' )")
    cursor.execute("INSERT INTO translations VALUES ('2', 'Umsatzart', 'Transaction Type', '' )")
    cursor.execute("INSERT INTO translations VALUES ('3', 'Begünstigter / Auftraggaber', 'Transaction Type', '' )")
    cursor.execute("INSERT INTO translations VALUES ('4', 'Verwendungszweck', 'Usage','Intended purpose memo' )")
    cursor.execute("INSERT INTO translations VALUES ('5', 'Kundenreferenz', 'Customer reference', '' )")
    cursor.execute("INSERT INTO translations VALUES ('6', 'Mandatsreferenz', 'Mandate reference', '' )")
    cursor.execute("INSERT INTO translations VALUES ('7', 'Gläubiger ID', 'Creditor identifier', '' )")
    cursor.execute("INSERT INTO translations VALUES ('8', 'Fremde Gebühren', 'Foreign fees', '' )")
    cursor.execute("INSERT INTO translations VALUES ('9', 'Betrag', 'Sum', '' )")
    cursor.execute("INSERT INTO translations VALUES ('10', 'Abweichender Empfänger', 'Transaction Type', '' )")
    cursor.execute("INSERT INTO translations VALUES ('11', 'Anzahl der Aufträge', 'No of orders', '' )")
    cursor.execute("INSERT INTO translations VALUES ('12', 'Anzahl der Schecks', 'No of checks', '' )")
    cursor.execute("INSERT INTO translations VALUES ('13', 'Soll', 'Debit', '' )")
    cursor.execute("INSERT INTO translations VALUES ('14', 'Haben', 'Credit', '' )")
    cursor.execute("INSERT INTO translations VALUES ('15', 'Währung', 'Currency', '' )")

    conn.commit()

    conn.close()


if __name__ == '__main__':
    translate_column_names()


