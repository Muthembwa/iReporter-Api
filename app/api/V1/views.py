from flask_restful import Api, Resource 
from flask import jsonify, make_response, request
import datetime

Red_flags=[{'flag_id':1,  
            'createdBy' : 'jafi',
            'type' : 'red-flags',
            'Location':'Thika',
            'status' : 'pending',
            'Comment':'dfffsfsfdsfsdfsdfdsfdfsdffdffdfdfffsdffffdf',
            }]
class RedFlags(Resource):
    def __init__(self):
        self.db = Red_flags
        self.id=len(Red_flags)+1
        
    def Post(self):
        data = {
            'Id' : self.id,
            'createdOn' : datetime.datetime.utcnow(),
            'createdBy' : request.json['createdBy'],
            'type' : 'red-flags',
            'location' : request.json['location'],
            'status' : 'pending',
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

    def Get(self):
        return make_response(jsonify({
            "status":200,
            "Red-Flags":self.db
        }),200)

class RedFlag(Resource):
    def __init__(self, flag_id):
        self.db = Red_flags
        self.flag_id=len(Red_flags)+1

    def Get(self):
        for flag in self.db:
            if flag ['flag_id']==self.flag_id:
                return flag
        return {'flag_id': None}, 404
















