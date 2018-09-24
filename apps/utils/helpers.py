from datetime import datetime
from datetime import date
import json
import hashlib


def json_converter(o):
	if isinstance(o, date):
		return str(o)

	if isinstance(o, datetime):
		return str(o)


def rest_repack(columns, rows, pack_array=True):
	'''
	Wrap data from the database into a dictionary. 
	'''
	if pack_array:
		payload = []
		for row in rows:
			payload.append(dict(zip(columns, row)))
	else:
		payload = dict(zip(columns, rows))

	return payload


def rest_render(payload):
	'''
	Wrapping dict becomes json type.
	Used when returning a response.
	'''
	return json.dumps(payload, default=json_converter)


def password_salt(raw_password):
	return hashlib.sha224(raw_password.encode('utf-8')).hexdigest()


def password_correctly(raw_password, password):
	return hashlib.sha224(raw_password.encode('utf-8')).hexdigest() == password