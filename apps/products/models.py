from apps import connector

def product_list(query=None):
	sql = """
		SELECT * FROM product;
	"""

	try:
		conn = connector.connect()
		cur = conn.cursor()

		cur.execute(sql)
		rows = cur.fetchall()
		conn.close()

		return rows
	except:
		return False

def product_add(data):
	name = data.get('name')
	cost = data.get('cost')
	final_price = data.get('final_price')
	stock = data.get('stock')
	minimum_stock = data.get('minimum_stock')

	sql = """
	INSERT INTO product (name, cost, final_price, stock, minimum_stock)
	VALUES (%s, %s, %s, %s, %s);
	"""
	try:
		conn = connector.connect()
		cur = conn.cursor()

		cur.execute(sql, (name, cost, final_price, stock, minimum_stock))

		conn.commit()
		conn.close()

		return True
	except:
		return False


def product_detail(id):
	sql = """
	SELECT * FROM product WHERE id=%s;
	"""
	try:
		conn = connector.connect()
		cur = conn.cursor()

		cur.execute(sql, (id,))
		row = cur.fetchone()
		
		cur.close()
		conn.close()

		return row
	except Exception as e:
		raise Exception(str(e))


def product_edit(data, id):
	sql = """
	UPDATE product SET name=%s, cost=%s, final_price=%s, stock=%s, minimum_stock=%s  
	WHERE id=%k;
	"""
	try:
		conn = connector.connect()
		cur = conn.cursor()

		cur.execute(sql, 
			(data.get('name'), 
			 data.get('cost'), 
			 data.get('final_price'), 
			 data.get('stock'), 
			 data.get('minimum_stock'), 
			 id)
		)

		conn.commit()
		cur.close()
		conn.close()

		return product_detail(id)
	except Exception as e:
		raise Exception(str(e))


def dummy_product_add():
	datas = [{
		"name": "product " + str(i+1),
		"cost": i+1,
		"final_price": i+1,
		"stock": i+1,
		"minimum_stock": i+1
	} for i in range(100)]

	for data in datas:
		product_add(data)




