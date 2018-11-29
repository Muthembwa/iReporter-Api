from flask_restful import Api, Resource 
from flask import jsonify, make_response, request
import datetime

Red_flags=[]
class iReporter(Resource):
    def __init__(self):
        self.db = Red_flags
        self.id=len(Red_flags)+1
        
    def post(self):
        data = {
            'Id' : self.id,
            'createdOn' : datetime.datetime.utcnow(),
            'createdBy' : request.json['createdBy'],
            'type' : 'red-flags',
            'location' : request.json['location'],
            'status' : "pending",
            'images' : request.json['images'],
            'videos' : request.json['videos'],
            'title' : request.json['title'],
            'comment' : request.json['comment']
       }
        self.db.append(data)
        success_message={
            "Id":self.id,
            "message":"Your Report Has Been Saved Successfully"
        }      
        return make_response(jsonify({
           "status" : 201,
           "data" : success_message
        }), 201) 