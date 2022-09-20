import psycopg2

from psycopg2.extras 	import RealDictCursor
from model.user 		import User 	as UserModel
from helper.response	import Response as ResponseHelper
from helper.db			import DB 		as DbHelper

class User:

# get

	async def get( uid : str = None ):

		if uid is None:

			return ResponseHelper.create( 500, 'Missing parameter' )

		try:

			with await DbHelper.connect() as connection:
		
				with connection.cursor( cursor_factory=RealDictCursor ) as cursor:

					cursor.execute( 'SELECT * from "user" where uid=%s', ( uid, ) )

					row = cursor.fetchmany(1)

					return ResponseHelper.create( 200, row )

		except ( Exception, psycopg2.Error ) as error:

				return ResponseHelper.create( 500, error.args[0] )

# list

	async def list():
		
		try:
			
			with await DbHelper.connect() as connection:
		
				with connection.cursor( cursor_factory=RealDictCursor ) as cursor:

					cursor.execute( 'SELECT * from "user" order by username' )

					rows = cursor.fetchall()

					return ResponseHelper.create( 200, rows )

		except ( Exception, psycopg2.Error ) as error:

				return ResponseHelper.create( 500, error.args[0] )


# delete

	async def delete( uid : str ):

		if uid is None:

			return ResponseHelper.create( 500, 'Missing parameter' )

		try:
			
			with await DbHelper.connect() as connection:
		
				with connection.cursor() as cursor:

					cursor.execute( 'DELETE from "user" where uid=%s', (uid,) )					

					return ResponseHelper.create( 200, cursor.rowcount )

		except ( Exception, psycopg2.Error ) as error:

				return ResponseHelper.create( 500, error.args[0] )

# post

	async def post( userModel : UserModel ):

		if userModel is None:

			return {'Missing parameter'}

		try:
			
			with await DbHelper.connect() as connection:
		
				with connection.cursor() as cursor:

					cursor.execute( 'insert into "user" (uid, username, password) values (%s, %s, %s)', ( userModel.uid, userModel.username, userModel.password ) )

					return ResponseHelper.create( 200, cursor.rowcount )

		except ( Exception, psycopg2.Error ) as error:

			return ResponseHelper.create( 500, error.args[0] )
