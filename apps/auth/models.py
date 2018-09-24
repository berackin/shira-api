from apps import connector
from apps.utils import helpers
from datetime import datetime


def user_detail(username):
	sql = """SELECT username, email, first_name, last_name, created, is_active FROM "user" WHERE username=%s;"""
	try:
		conn = connector.connect()
		cur = conn.cursor()

		cur.execute(sql, (username,))
		raw = cur.fetchone()

		cur.close()
		conn.close()

		return raw
	except Exception as e:
		raise Exception(str(e))


def user_register(body):
	sql = """
	INSERT INTO "user" (username, email, password, first_name, last_name, created, is_active)
	VALUES (%s, %s, %s, %s, %s, %s, %s);
	"""
	try:
		conn = connector.connect()
		cur = conn.cursor()

		cur.execute(sql, (
			body.get('username'),
			body.get('email'),
			helpers.password_salt(body.get('password')),
			body.get('first_name'),
			body.get('last_name'),
			datetime.now(),
			True
		))

		conn.commit()
		conn.close()

		return user_detail(body.get('username'))

	except Exception as e:
		raise Exception(str(e))



