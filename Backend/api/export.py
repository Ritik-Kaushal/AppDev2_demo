from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required
from utils.role_required import role_required
from utils.celery.tasks import export_data
from instance.api import api
import time

class ExportAPI(Resource):
    '''
        API to trigger export of data.
        Only Admin can access this
    '''
    @jwt_required()
    @role_required(['ADMIN'])
    def get(self):
        res = export_data.delay()
        while not res.ready():
            print("Still in progress")
            time.sleep(2)

        if not res.get()[0] : 
            return {"message" : res.get()[1]},400
        else:
            return {"message" : res.get()[1]},200

api.add_resource(ExportAPI,'/export')