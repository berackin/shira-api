from apps import settings
from apps.utils import decorators, helpers
from apps.auth import models

app = settings.APP 


@app.route('/auth/register', method='POST')
@decorators.rest_inject()
def user_register(request, response, body):
	row = models.user_register(body)

	payload = helpers.rest_repack(
		('username', 'email', 'first_name', 
		 'last_name', 'created', 'is_active'), row, False)

	return helpers.rest_render(payload)

