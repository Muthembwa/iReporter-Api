from flask_restful import Api, Resource 
from flask import Blueprint


version_one = Blueprint('api_V1', __name__, url_prefix='/api/V1')
api = Api(version_one)

