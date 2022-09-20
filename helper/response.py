from model.response import Response 

class Response:

	def create( code : int, payload : object ) -> Response:

		response = Response()

		response.code 		= code
		response.payload 	= payload
		
		return response