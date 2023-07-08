from flask_restful import Resource
from flask import request, jsonify
from instance.api import api
from instance.database import db
from application.models import Testimonial
from flask_jwt_extended import get_jwt_identity, jwt_required

class TestimonialUserApi(Resource):
    '''
        API for testimonials of a general user
    '''
    def get(self):
        try :
            testimonials = Testimonial.query.filter_by(approved = True).all()
            result = [{
                'id' : testimonial.id,
                'content' : testimonial.content,
                'username' : testimonial.user.email 
            } for testimonial in testimonials]

            return {"testimonials" : result} , 200
        except Exception as e :
            print(e)
            return {'message' : "Internal Server Error"} , 500
    
    @jwt_required()
    def post(self):
        try:
            current_user = get_jwt_identity()
            data = request.get_json()

            content = data.get('content')
            user_id = current_user.get('id')

            if(content and user_id):
                testimonial = Testimonial(
                    content = content,
                    user_id = user_id
                )

                db.session.add(testimonial)
                db.session.commit()
                return {"message" : "Successfully Created"} , 200

            else:
                return {'message': 'Missing details'}, 400

            

        except Exception as e:
            print(e);
            return {'message' : "Internal Server Error"} , 500
    

api.add_resource(TestimonialUserApi,'/testimonial')