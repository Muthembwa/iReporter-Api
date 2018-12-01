from flask_restful import Api, Resource 
from flask import jsonify, make_response, request
import datetime

from .models import IncidenceModel


class RedFlags(Resource):
    def __init__(self):
        self.db = IncidenceModel()
         

    def post(self): 
        data = request.get_json(force=True)
        CreatedBy = data['CreatedBy']
        IncidenceType = data['IncidenceType']
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

    def get(self):
        resp=self.db.view()
        return make_response(jsonify({
            "Status" : 200,
            "All Red Flags":resp
        }),200)

class RedFlag(Resource):
    def __init__(self):
        self.db = IncidenceModel()      

    def get(self, Id): 
        Flag=self.db.viewOne(Id)
        return make_response(jsonify({
            "Status" : 200,
            "your entry is": Flag
        }),200)

   

    
















