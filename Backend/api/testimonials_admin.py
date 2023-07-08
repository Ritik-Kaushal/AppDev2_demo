from flask_restful import Resource
from flask import request, jsonify
from instance.api import api
from instance.database import db
from application.models import Testimonial
from flask_jwt_extended import get_jwt_identity, jwt_required
from utils.role_required import role_required

class TestimonialAdminApi(Resource):
    '''
        API for testimonials of a general user
    '''
    @jwt_required()
    @role_required(['ADMIN'])
    def get(self):
        try :
            testimonials = Testimonial.query.filter_by(approved = False).all()
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
    @role_required(['ADMIN'])
    def put(self):
        try:
            current_user = get_jwt_identity()
            data = request.get_json()
            
            testimonial_id = data.get('testimonial_id')
            status = data.get('status',False)
            user_id = current_user.get('id')

            try:
                testimonial_id = int(testimonial_id)
                status = bool(status)

            except Exception as e:
                print(e)
                return {'message' : "Invalid data in fields"} , 400
            
            if(user_id and testimonial_id):
                testimonial = Testimonial.query.filter_by(id = testimonial_id).first()
                if not testimonial:
                    return {'message': 'Testimonial not found'}, 404

                testimonial.approved = status
                db.session.commit()
               
                return {"message" : "Successfully Updated"} , 200

            else:
                return {'message': 'Missing details'}, 400

        except Exception as e:
            print(e)
            return {'message' : "Internal Server Error"} , 500
    

api.add_resource(TestimonialAdminApi,'/admin/testimonial')