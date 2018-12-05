from flask_restful import Api, Resource 
from flask import jsonify, make_response, request
import datetime

from .models import RedFlagModel

new_flag = RedFlagModel()

class RedFlags(Resource, RedFlagModel):
    def __init__(self):
        self.db = RedFlagModel(CreatedBy, Location, Status, Comment)
        self.CreatedBy = CreatedBy
        self.Location = Location
        self.Status = Status
        self.Comment = Comment


    def post(self): 
        data = request.get_json(force=True)
    
        CreatedBy = data['CreatedBy']
        Location = data['Location']
        Status = data['Status']
        Comment = data ['Comment'] 

        data ={
            'CreatedBy':CreatedBy,
            'Location':Location,
            'Status': Status,
            'Comment':Comment
        }
 
        new_flag = RedFlagModel(CreatedBy, Location, Status, Comment)
        resp = new_flag.save(data)
         
        return make_response(jsonify({
           "Status" : 201,
           "data" : success_message
        }), 201)  

    def get(self):
        resp =self.db.view()
        return make_response(jsonify({
            "successfully deleted"
        }),204)

class RedFlag(Resource):
    def __init__(self):
        self.db = RedFlagModel()      

    def get(self, Id): 
        Flag =self.db.viewOne(Id)
        if not Flag: 
            return make_response(jsonify({"Flag does not exist":404}), 404)
        return make_response(jsonify({
            "Status" : 200,
            "data": Flag
        }),200)
        
    def delete(self, Id):
        Flag = self.db.deleteOne(Id)
        return make_response(jsonify({
            "successfully deleted"
        }),204)


    def patch( self, Id ):
        Flag =self.db.viewOne(Id)
        if not Flag: 
            return make_response(jsonify({"Flag does not exist":404}), 404)
        else:
            data = Flag.update(request.get_json()) 
            return make_response(jsonify({
                "status":200,
                "data":data
            }),200)

 











  