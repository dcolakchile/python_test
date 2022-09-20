import psycopg2
import json

from psycopg2.extras 	import RealDictCursor
from model.product 		import Product 	as ProductModel
from helper.response	import Response as ResponseHelper
from helper.db			import DB 		as DbHelper

class Product:

# get

	async def get( id : str = None ):

		if id is None:

			return ResponseHelper.create( 500, 'Missing parameter' )

		try:

			with await DbHelper.connect() as connection:
		
				with connection.cursor( cursor_factory=RealDictCursor ) as cursor:

					cursor.execute( 'SELECT * from product where id=%s', ( id, ) )

					row = cursor.fetchmany(1)

					return ResponseHelper.create( 200, row )

		except ( Exception, psycopg2.Error ) as error:

				return ResponseHelper.create( 500, error.args[0] )

# list

	async def list():
		
		try:
			
			with await DbHelper.connect() as connection:
		
				with connection.cursor( cursor_factory=RealDictCursor ) as cursor:

					cursor.execute( 'SELECT * from product order by id' )

					rows = cursor.fetchall()

					return ResponseHelper.create( 200, rows )

		except ( Exception, psycopg2.Error ) as error:

				return ResponseHelper.create( 500, error.args[0] )


# delete

	async def delete( id : str ):

		if id is None:

			return ResponseHelper.create( 500, 'Missing parameter' )

		try:
			
			with await DbHelper.connect() as connection:
		
				with connection.cursor() as cursor:

					cursor.execute( 'DELETE from product where id=%s', (id,) )					

					return ResponseHelper.create( 200, cursor.rowcount )

		except ( Exception, psycopg2.Error ) as error:

				return ResponseHelper.create( 500, error.args[0] )

# post

	async def post( productModel : ProductModel ):

		if productModel is None:

			return {'Missing parameter'}

		try:
			
			with await DbHelper.connect() as connection:
		
				with connection.cursor() as cursor:

					cursor.execute( 'insert into product (id, name, uom, category_name, is_producible, is_purchasable, type, purchase_uom, batch_tracked, additional_info, purchase_uom_conversion_rate, created_at, updated_at) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
					(productModel.id, productModel.name, productModel.uom, productModel.category_name, productModel.is_producible, productModel.is_purchasable, productModel.type, productModel.purchase_uom, productModel.batch_tracked,productModel.additional_info,productModel.purchase_uom_conversion_rate, productModel.created_at, productModel.updated_at))

					for productVariant in productModel.variants:

						cursor.execute( 'insert into productvariant (id, product_id, sku, sales_price, purchase_price, type, created_at, updated_at, config_attributes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s )',
						(productVariant.id, productVariant.product_id, productVariant.sku, productVariant.sales_price, productVariant.purchase_price, productVariant.type, productVariant.created_at, productVariant.updated_at, json.dumps( productVariant.config_attributes, default=vars ) ))

					return ResponseHelper.create( 200, cursor.rowcount )

		except ( Exception, psycopg2.Error ) as error:

			return ResponseHelper.create( 500, error.args[0] )
