import json
from functools import wraps
from bottle import response, request


def rest_inject(resp_status=200, resp_ctype='application/json'):
	'''
	Decoration for the view function that handles 
	requests and response bodies for rest purposes.
	'''
	def rest(f):
		@wraps(f)
		def wrapped(*args, **kwargs):
			if request.headers.get('Content-Type') != 'application/json':
				response.status = 400
				return {"error": "Bad Request"}

			response.status = resp_status
			response.content_type = 'application/json'

			kwargs['request'] = request
			kwargs['response'] = response
			kwargs['body'] = request.json

			try:
				return f(*args, **kwargs)
			except Exception as e:
				response.status = 400
				return {"error": str(e)}

		return wrapped
	return rest