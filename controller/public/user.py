from fastapi 			import APIRouter, Depends, Form
from fastapi.security 	import OAuth2PasswordBearer

router = APIRouter()

@router.post( "/token" )
def token( username : str = Form(), password : str = Form()):

	# Go to the db, use hashed passwords etc. :-)

	if username == 'damir' and password == 'damir':
		token = 'can_readwrite'

	if username == 'ana' and password == 'ana':
		token = 'can_read'

	return {"access_token": token, "token_type": "bearer"}
