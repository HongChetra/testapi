from flask_restful import Resource, reqparse 
from models.user import UserModel

	
	
class UserRegister(Resource):

	parser = reqparse.RequestParser()

	parser.add_argument('username',
		type=str,
		required=True,
		help='Can not be blank'
	)
	parser.add_argument('password',
		type=str,
		required=True,
		help= 'can not leave it blank'
	)

	def post(self):

		data = UserRegister.parser.parse_args()  # Get the json request
		
		if UserModel.find_by_username(data['username']): # if.. is not None: to check if user is existed
			return {"message": "that username is already token."}, 400 

		user = UserModel(**data)
		user.save_to_db()

		return {"message": "User has been created!"}, 201