from functools import wraps
from flask_jwt_extended import get_jwt_identity
from application.models import User

def role_required(roles):
    """
        Decorator to verify roles of user. 
        Must be used after jwt_required decorator.
        
        PARAMS
        1. roles : A list of roles which are accepted
    """
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                curr_user = get_jwt_identity()
                id = curr_user.get('id')

                if not id:
                    return {'msg' : 'Invalid Token'} , 403

                user = User.query.filter_by(id = id).first();
                if not user:
                    return {'msg' : 'User not found.'} , 404

                if not user.role in roles:
                    return {'msg' : 'Unauthorised.'} , 401
                return fn(*args, **kwargs)

            except Exception as e:
                return {'msg' : 'Internal Server Error'} , 500
        return wrapper
    return decorator
