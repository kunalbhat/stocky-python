import json
import sqlite3
import ystockquote

from flask import Flask, url_for, render_template, request, g

# Setup Flask
app = Flask(__name__)

# Index page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/portfolio/')
def portfolio():
    # Setup sqlite
    conn = sqlite3.connect('portfolios.db')

    c = conn.cursor()

    c.executemany('SELECT * FROM stocks')

    print(c)

    return json.dumps()

    c.close()

@app.route('/symbol/<string:symbol>')
def symbol(symbol):

    last_trade_price = ystockquote.get_last_trade_price(symbol)

    return json.dumps({'last_trade_price': last_trade_price})
    pass

if __name__ == "__main__":
    app.run()

