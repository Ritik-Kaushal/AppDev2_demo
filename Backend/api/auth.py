from flask_restful import Resource
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

from application.models import User
from instance.database import db
from instance.api import api

from datetime import timedelta
from utils.mail.reminder_mail import send_remainder_emails

class UserRegistrationAPI(Resource):
    '''
        API to register user
    '''
    
    def post(self):
        # Get the request data
        data = request.get_json()

        if data.get('email') and data.get('password'):
            # Check if the user already exists
            if User.query.filter_by(email=data['email']).first():
                return {'message': 'User already exists'}, 409

            # Create a new user
            user = User(
                email=data['email'],
                password=generate_password_hash(data['password']),
                active=True,
                role="END_USER"
            )
            db.session.add(user)
            db.session.commit()

            return {'message': 'User registered successfully'}, 201
        else:
            return {'message': 'Missing details'}, 400


# Define the user login resource
class UserLoginAPI(Resource):
    '''
        API to login user and get token
    '''
    def post(self):
        # Get the request data
        data = request.get_json()

        if data.get('email') and data.get('password'):
            # Find the user by email
            user = User.query.filter_by(email=data['email']).first()

            # Check if the user exists and the password is correct
            if user and check_password_hash(user.password, data['password']):

                identity = {'id': user.id, 'email': user.email}

                # Generate an access token
                access_token = create_access_token(identity=identity, expires_delta=timedelta(2))

                return {'message': 'User logged in successfully', 'access_token': access_token}

            return {'message': 'Invalid email or password'}, 401
        else:
            return {'message': 'Missing details'}, 400


api.add_resource(UserRegistrationAPI, '/register')
api.add_resource(UserLoginAPI, '/login')
