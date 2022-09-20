import psycopg2

class DB:

		# TODO:- get the connection information from the local config file

		async def connect():
			
			return psycopg2.connect( dbname='damircolak', user='postgres', password='damir95', host='localhost', port=5433 )
