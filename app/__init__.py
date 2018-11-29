from flask import Flask
from flask_restful import Api, Resource

from .api.V1.views import iReporter

def create_app():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(iReporter, '/flags')
    return app