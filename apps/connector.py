import psycopg2
from apps.settings import DATABASES

def connect():
	try:
		conn = psycopg2.connect(
			host=DATABASES['HOST'],
			database=DATABASES['NAME'],
			user=DATABASES['USER'],
			password=DATABASES['PASSWORD'])

		return conn
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)


