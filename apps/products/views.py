import json
from apps import settings
from apps.products import models
from apps.utils import decorators, helpers

app = settings.APP 


@app.route('/products', method='GET')
@decorators.rest_inject()
def product_list(request, response, body):
	rows = models.product_list()

	payload = helpers.rest_repack(
		('id', 'name', 'cost', 
		 'final_price', 'stock', 
		 'minimum_stock'), rows)

	return helpers.rest_render(payload)


@app.route('/products', method='POST')
@decorators.rest_inject(resp_status=201)
def product_add(request, response, body):
	models.product_add(body)
	return helpers.rest_render(body)


@app.route('/products/<id>', method="GET")
@decorators.rest_inject()
def product_detail(request, response, body, id):
	row = models.product_detail(id)
	payload = helpers.rest_repack(('id', 'name', 'cost', 
			   		  'final_price', 'stock', 
			   		  'minimum_stock'), row, False)

	return helpers.rest_render(payload)


@app.route('/products/<id>', method='PUT')
@decorators.rest_inject()
def product_edit(request, response, body, id):
	models.dummy_product_add()
	# row = models.product_edit(body, id)
	# payload = bottils.http.rest_repack(
	# 	('id', 'name', 'cost', 
	# 	 'final_price', 'stock', 
	# 	 'minimum_stock'), row, False)

	return helpers.rest_render({"ok": True})


@app.route('/products/<id>', method='DELETE')
@decorators.rest_inject()
def product_delete(request, response, body, id):
	pass