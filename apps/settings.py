from bottle import Bottle 


APP = Bottle()

DEBUG = True
HOST = 'localhost'
PORT = 9000

BASE_URL = f'{HOST}:{PORT}'

DATABASES = {
	'HOST': 'localhost',
	'NAME': 'shira_db',
	'USER': 'postgres',
	'PASSWORD': 'root',
	'PORT': '5432'
}

# Call all views in here from your apps.
from apps.auth.views import *
from apps.products.views import *