import json

from fastapi 			import APIRouter, Depends, HTTPException
from types 				import SimpleNamespace

from service.api.oauth 			import api_can_read, api_can_write
from service.db.product 		import Product 	as ProductDbService
from helper.response			import Response as ResponseHelper
from model.product				import Product 	as ProductModel

router = APIRouter()

@router.get( "/" )
async def get( uid : str = None, token : str = Depends(api_can_read) ):

	if uid is None:

		return ResponseHelper.create( 404, 'Missing parameter' )

	response = await ProductDbService.get( uid )
	
	if response.code != 200:
		raise HTTPException(status_code=response.code, detail=response.payload)

	return response

@router.get( "/list" )
async def list( token : str = Depends(api_can_read) ):

	return await ProductDbService.list()

@router.delete( "/" )
async def delete( uid : str, token : str = Depends(api_can_write) ):

	if uid is None:

		return {'Missing parameter'}

	return await ProductDbService.delete( uid )

@router.post( "/create" )
async def add( productModel : ProductModel, token : str = Depends(api_can_write) ):

	# We could use token to see the exact roles user has and fine tune everything :-)

	if productModel is None:

		return {'Missing parameter'}

	return await ProductDbService.post( productModel )


