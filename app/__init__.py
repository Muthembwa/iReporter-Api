from flask import Flask, Blueprint
from flask_restful import Api, Resource
from flask_script import Manager
import os
import unittest

#local imports
from .api.V1.views import RedFlags, RedFlag #RedFlagComment
from instance.config import app_config
from .api.V1 import version_one as V1

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config['testing'])
    app.config.from_pyfile('config.py')
    app.register_blueprint(V1)
    api = Api(app)
        
    api.add_resource(RedFlags, '/red-flags')
    api.add_resource(RedFlag, '/red-flag/<int:Id>')
    #api.add_resource(RedFlagComment, '/red-flag/<int:Id>/comment')
    return app
def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover('app/tests/V1/', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1