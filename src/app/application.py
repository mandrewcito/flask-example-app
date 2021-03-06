from flask import Flask,jsonify

from app.responses.default import DefaultResponse

from app.class_module.controllers import ClassModule as ClassModule
from app.script_module.controllers import script_module as script_module
from app.errors.invalid_usage import InvalidUsage as InvalidUsage

from app.api.v1.api_blueprint import ApiBlueprint as V1
from app.api.v2.api_blueprint import ApiBlueprint as V2

class ExampleApi(Flask):
    def __init__(self,configuration):
        super(ExampleApi, self).__init__(__name__)

        # Default response register
        self.response_class = DefaultResponse

        # Register api with blueprints and views
        self.register_blueprint(V1())
        self.register_blueprint(V2())

        # Register modules as a class instance
        self.register_blueprint(ClassModule())

        # Register modules as an instantiated object
        self.register_blueprint(script_module)

        # Register error handler
        self.register_error_handler(InvalidUsage, self.handle_invalid_usage)

        # Add url - raises error handler -
        self.add_url_rule('/error/custom/foo', view_func=self.get_foo)

    def handle_invalid_usage(self,error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    def get_foo(self):
        raise InvalidUsage('This view is gone', status_code=410)
