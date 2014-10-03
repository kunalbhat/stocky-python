import sqlite3

conn = sqlite3.connect('porfolios.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, shares real, price real, commission real)''')

conn.commit()

conn.close()

