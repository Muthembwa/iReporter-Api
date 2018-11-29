from flask import Flask
from flask_restful import Api, Resource

from .api.V1.views import RedFlags, RedFlag

def create_app():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(RedFlags, '/flags')
    api.add_resource(RedFlag, '/flag/<int:flag_id>')
    return app