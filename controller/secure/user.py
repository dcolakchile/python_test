from fastapi 			import APIRouter, Depends, HTTPException
from fastapi.security 	import OAuth2PasswordBearer

from model.user 				import User 	as UserModel
from service.api.oauth 			import api_can_read, api_can_write
from service.db.user 			import User 	as UserDbService
from helper.response			import Response as ResponseHelper

router = APIRouter()

@router.get( "/" )
async def get( uid : str = None, token : str = Depends(api_can_read) ):

	if uid is None:

		return ResponseHelper.create( 404, 'Missing parameter' )

	response = await UserDbService.get( uid )
	
	if response.code != 200:
		raise HTTPException(status_code=response.code, detail=response.payload)

	return response

@router.get( "/list" )
async def list( token : str = Depends(api_can_read) ):

	return await UserDbService.list()

@router.delete( "/" )
async def delete( uid : str, token : str = Depends(api_can_write) ):

	if uid is None:

		return {'Missing parameter'}

	return await UserDbService.delete( uid )

@router.post( "/" )
async def add( userModel : UserModel, token : str = Depends(api_can_write) ):

	# We could use token to see the exact roles user has and fine tune everything :-)

	if userModel is None:

		return {'Missing parameter'}

	return await UserDbService.post( userModel )


