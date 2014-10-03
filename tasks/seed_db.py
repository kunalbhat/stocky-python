import sqlite3

conn = sqlite3.connect('porfolios.db')

c = conn.cursor()

purchases = [('2013-06-28', 'BUY', 'INTC', 250, 24.085, 9.99),
             ('2013-09-05', 'BUY', 'FBIOX', 30, 168.02, 19.99),
            ]

c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?,?)', purchases)

conn.commit()

conn.close()

