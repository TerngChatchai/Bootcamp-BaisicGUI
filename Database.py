# Database.py

import sqlite3

conn = sqlite3.connect('product-database.sqlite3')
c = conn.cursor()



#CREATE TABLE
c.execute("""CREATE TABLE IF NOT EXISTS transaction_history (
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				tid TEXT,
				stamp TEXT,
				product TEXT,
				price REAL,
				quan REAL,
				total REAL )""")

print('success')

def insert_transaction(data):
	ID = None
	tid = data['tid']
	stamp = data['stamp']
	product = data['product']
	price = data['price']
	quan = data['quan']
	total = data['total']

	with conn:
		command = 'INSERT INTO transaction_history VALUES (?,?,?,?,?,?,?)'
		c.execute(command,(ID,tid,stamp,product,price,quan,total))
		conn.commit()
	print('inserted!!!')

def view_transaction():
	with conn:
		c.execute("SELECT * FROM transaction_history")
		data = c.fetchall()
		print(data)



transaction = {'tid': '12331241',
				'stamp': '2022-11-06 11:23:34',
				'product' : 'Bow tie',
				'price' : 1000,
				'quan': 5,
				'total' : 5000
				}


#insert_transaction(transaction)
view_transaction()