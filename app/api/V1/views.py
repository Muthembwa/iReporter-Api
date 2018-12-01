from flask_restful import Api, Resource 
from flask import jsonify, make_response, request
import datetime

from .models import IncidenceModel


class IncidentsResource(Resource, IncidenceModel):
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
            "data":resp,
            "message":"Your Report Has Been Saved Successfully"
        }      
        return make_response(jsonify({
           "status" : 201,
           "data" : success_message
        }), 201)  

    def get(self):
        resp=self.db.View()
        return make_response(jsonify({
            "self.db":resp
        }),200)

class IncidentResource(Resource,  IncidenceModel):
    def __init__(self, flag_id):
        self.db = Red_flags
        self.flag_id=len(Red_flags)+1

    def get(self):
        flag=next(filter(lambda x:x["flag_id"]== flag_id, None))
        return {'flag_id': self.db}, 200 if flag_id else 404

    def Post (self):
        if next(filter(lambda x:x["flag_id"]== flag_id, None)):
            return {'message':"An flag_id with '{}'already exixts".format(flag_id)},400
        
        data = request.get_json(force=True)
        CreatedBy = data["CreatedBy"]
        IncidenceType = data["IncidenceType"]
        Location = data["Location"]
        Status = data["Status"]
        Comment = data["Comment"] 

        resp= self.db.Save(CreatedBy, IncidenceType, Location, Status, Comment)     
        return make_response(jsonify({
            "message":"Your Report Has Been Saved Successfully",
            "Incident" : resp
        }), 201)

















