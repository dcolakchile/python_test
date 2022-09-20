from fastapi 			import Header, Depends, HTTPException
from fastapi.security 	import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def api_can_read( token : str = Depends(oauth2_scheme) ):
	
	if token != "can_read" and token != "can_readwrite":
		raise HTTPException(status_code=404, detail="You can't read, back to school for you")


async def api_can_write( token : str = Depends(oauth2_scheme) ):

	if token != "can_write" and token != "can_readwrite":
		raise HTTPException(status_code=404, detail="You can't write, back to school for you")