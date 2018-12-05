from flask_restful import Api, Resource 
from flask import jsonify, make_response, request
import datetime

from .models import RedFlagModel



class RedFlags(Resource):
    def __init__(self,CreatedBy, Location, Status, Comment):
        self.db = RedFlagModel()
         

    def post(self): 
        daatedBy = data['CreatedBy']
        Locta = request.get_json(force=True)
        Creation = data['Location']
        Status = data['Status']
        Comment = data['Comment'] 


        new_flag = RedFlagModel(data)
        resp = self.db.save(new_flag)
        success_message={
            "The Redflag": new_flag 
        }      
        return make_response(jsonify({
           "Status" : 201,
           "data" : success_message
        }), 201)  

    def get(self):
        resp =self.db.view()
        return make_response(jsonify({
            "Status" : 200,
            "All Red Flags":resp
        }),200)

class RedFlag(Resource):
    def __init__(self):
        self.db = RedFlagModel()      

    def get(self, Id): 
        Flag =self.db.viewOne(Id)
        if not Flag: 
            return make_response(jsonify({"Flag does not exist":404}), 404)
        return make_response(jsonify({
            "Status" : 200,
            "your entry is": Flag
        }),200)
        
    def delete(self, Id):
        Flag = self.db.deleteOne(Id)
        return make_response(jsonify({
            "Status" : 200,
            "successfully deleted": self.db
        }),200)


    def patch( self, Id ):
        Flag =self.db.viewOne(Id)
        if not Flag: 
            return make_response(jsonify({"Flag does not exist":404}), 404)
        else:
            data = Flag.update(request.get_json()) 
            return make_response(jsonify({
                "status":200,
                "Comment edited successfuly":Flag
            }),200)

 











  