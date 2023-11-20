from flask import Blueprint, jsonify, Flask
from orm.sql_models.user import User
from setting import Config
# api.py

from flask import Blueprint, jsonify, Flask
from flask_restx import Api, Resource, fields

api_bp = Blueprint('user', __name__)
# Flask-RESTx setup
api = Api(api_bp, title='User API', version='1.0', description='CRUD operations for User')
session = Config.Session()
# Define the User data model for request and response
user_model = api.model('User', {
    'User_Id': fields.Integer(),
    'User_name': fields.String(required=True, description='User name'),
    'Phone_Number': fields.String(required=True, description='Phone number'),
    'Email_Id': fields.String(required=True, description='Email address'),
    'create_date': fields.DateTime(),
    'update_date': fields.DateTime(),
})

# Resource for handling CRUD operations on User
class UserResource(Resource):
    @api.marshal_with(user_model, envelope='data')
    def get(self, user_id):
        user = User.query.get(user_id)
        if user:
            return user
        else:
            api.abort(404, message=f"User with id {user_id} not found")
    @api.marshal_with(user_model, envelope='data')
    def post(self):
        new_user = User(
            User_name=api.payload['User_name'],
            Phone_Number=api.payload['Phone_Number'],
            Email_Id=api.payload['Email_Id']
        )
        session.add(new_user)
        session.commit()
        return new_user, 201
    
# Resource for handling the creation of new users
class UserListResource(Resource):
    @api.marshal_with(user_model, envelope='data')
    def put(self, user_id):
        user = User.query.get(user_id)
        if user:
            user.User_name = api.payload['User_name']
            user.Phone_Number = api.payload['Phone_Number']
            user.Email_Id = api.payload['Email_Id']
            session.commit()
            return user
        else:
            api.abort(404, message=f"User with id {user_id} not found")

    def delete(self, user_id):
        user = User.query.get(user_id)
        if user:
            session.delete(user)
            session.commit()
            return {'message': f"User with id {user_id} deleted successfully"}
        else:
            api.abort(404, message=f"User with id {user_id} not found")


# Define API resources
api.add_resource(UserResource, '/user')
api.add_resource(UserListResource, '/users/<int:user_id>')

