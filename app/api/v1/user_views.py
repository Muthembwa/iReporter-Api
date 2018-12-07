from flask_restful import Api, Resource 
from flask import jsonify, make_response, request
import datetime

from .user_models import userModel

class user(Resource):
    def __init__(self):
        self.db= userModel()

def post(self): 
        data = request.get_json(force=True)
        UserName = data['CreatedBy']
        Name = data['IncidenceType']
        Location = data['Location']
        Status = data['Status']
        Comment = data['Comment'] 
         
        resp = self.db.save(CreatedBy, IncidenceType, Location, Status, Comment)
        success_message={
            "The Redflag":resp,
            "message":"Your Report Has Been Saved Successfully"
        }      
        return make_response(jsonify({
           "Status" : 201,
           "data" : success_message
        }), 201)  
