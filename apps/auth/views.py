from apps import settings

app = settings.APP 

@app.route('/auth/signin')
def signin():
	return {'name': "Yanwar"}


@app.route('/auth/token-auth')
def token_auth():
	return {}