import json


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
	return json.dumps(payload)