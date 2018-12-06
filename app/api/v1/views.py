from flask_restful import Api, Resource, reqparse, abort 
from flask import jsonify, make_response, request
import datetime


from .models import RedFlagModel


def abort_if_dont_exist(Id):
    if Id not in RedFlagModel.flags:
        abort (404, message = "Red-Flag {} doesnt exist".format(Id))


class RedFlags(Resource):
    def __init__(self):
        self.db = RedFlagModel.flags

    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('CreatedBy')
        parser.add_argument('Location') 
        parser.add_argument('Status') 
        parser.add_argument('Comment')
        args = parser.parse_args() 
        new_flag = RedFlagModel(CreatedBy= args['CreatedBy'],
                                Location = args['Location'],
                                Status = args['Status'], 
                                Comment =  args['Comment'])
        resp = self.db.append(new_flag.__dict__)
        return "Successful", 201
   

    def get(self):
        resp =self.db
        return  resp,200

class RedFlag(Resource):
    def __init__(self):
        self.db = RedFlagModel.flags

    def get(self, Id): 
        Flag = RedFlagModel.viewOne(Id)
        if not Flag: 
            return make_response(jsonify({"Flag does not exist":404}), 404)
        return make_response(jsonify({
            "Status" : 200,
            "data": Flag
        }),200)
        
    def delete(self, Id):
        Flag = RedFlagModel.viewOne(Id)
        if not Flag: 
            return "Flag does not exist", 404
        else:
            Flag = RedFlagModel.deleteOne(Id)
            return "Deleted successfully",200


    def patch( self, Id ):
        Flag = RedFlagModel.viewOne(Id)
        if not Flag: 
            return make_response(jsonify({"Flag does not exist":404}), 404)
        else:
            data = Flag.update(request.get_json()) 
            return make_response(jsonify({
                "status":200,
                "data":data
            }),200)

 











  