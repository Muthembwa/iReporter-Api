from flask_restful import Api, Resource 
from flask import Blueprint

from .views import IncidentsResource, IncidentResource

version_one = Blueprint('api_v1', __name__, url_prefix='/api/V1')
api = Api(version_one)

api.add_resource(IncidentsResource, '/Incidents')
api.add_resource(IncidentResource, '/Incident/')