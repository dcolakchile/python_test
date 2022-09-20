## To test just debug from vscode or go to the command line

uvicorn main:app

##  Swagger user/password for authentication

damir/damir : can read and write
ana/ANALYZE	: can only read

## How to test API

1. Authenticate through swagger with above mentioned user/passwords
2. Add record by using post (uid, username, password) where uid is guid/uuid 
	see https://www.guidgenerator.com/online-guid-generator.aspx)
3. Use get/list/delete ;-)

## Database connection info

Edit helper/db.py

##  Database create script

Check the db/init folder
