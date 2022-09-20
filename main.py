from fastapi 			import Depends, FastAPI
from fastapi.security 	import OAuth2PasswordBearer

from controller.public import user 		as publicUser
from controller.secure import user 		as secureUser
from controller.secure import product 	as secureProduct

from tests.products import *

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

# public API's

app.include_router(publicUser.router)

# secure API's

app.include_router(
    secureUser.router,
    prefix="/v1/user",
    tags=["user"],
    dependencies=[Depends(oauth2_scheme)]    
)

app.include_router(
    secureProduct.router,
    prefix="/v1/products",
    tags=["products"],
    dependencies=[Depends(oauth2_scheme)]    
)

# root API meethods

@app.get("/")
async def root():
    return {"message": "Hello handsome!"}

@app.get("/test")
async def test():
    return test_product_create()