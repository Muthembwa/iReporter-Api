from flask import Flask, Blueprint
from flask_restful import Api, Resource

#local imports
from .api.V1.views import RedFlags, RedFlag
from instance.config import app_config
from .api.V1 import version_one as V1

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config['development'])
    app.config.from_pyfile('config.py')
    app.register_blueprint(V1)
    api = Api(app)
    
    
    api.add_resource(RedFlags, '/red-flags')
    api.add_resource(RedFlag, '/red-flag/<int:Id>')
    return app