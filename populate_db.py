import sqlite3
import alpaca_trade_api as alp

KEY_ID = 'PK3KQZJHNQK2C0X0HTXE'
SECRET = 'uRrBvRRmPyfe2UFtKbp9j7lOlclvLt25BCrlfQO8'

connection = sqlite3.connect('/Users/justdanape/Documents/python_projects/app.db')
cursor = connection.cursor()

api = alp.REST(KEY_ID,SECRET,base_url='https://paper-api.alpaca.markets')
cursor.execute("""
               SELECT symbol, company FROM stock""")
rows = cursor.fetchall()

symbols = [row[0] for row in rows]

assets = api.list_assets()

for asset in assets:
    try:
        if asset.status == 'active' and asset.tradable and asset.symbol not in symbols:
            print(f"Added a new stock {asset.symbol} {asset.name}")
            cursor.execute("INSERT INTO stock (symbol, company) VALUES (?, ?)", (asset.symbol, asset.name))
    except Exception as e:
        print(asset.symbol)
        print(e)
connection.commit()    
#https://www.nasdaqtrader.com/dynamic/SymDir/nasdaqlisted.txt