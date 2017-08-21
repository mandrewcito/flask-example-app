from flask import Flask,jsonify,Blueprint

from app.v1.class_module.controllers import ClassModule as ClassModule
from app.v1.script_module.controllers import script_module as script_module

from app.v1.errors.invalid_usage import InvalidUsage as InvalidUsage

from app.v1.responses.default import DefaultResponse

class V1(Blueprint):
    def __init__(self):
        super(V1,self).__init__("v1 module",__name__,url_prefix='/v1')
 
        # Default response register
        self.response_class = DefaultResponse
        # Register modules as a class instance
        self.add_url_rule("/hello",view_func=self.hello,methods=['GET']) 

        # Register modules as an instantiated object
        #self.register_blueprint(script_module)
        
        # Register error handler
        self.record_once(lambda x: x.app.errorhandler(InvalidUsage)(self.handle_invalid_usage))

        # Add url - raises error handler -
        self.add_url_rule('/error/custom/foo', view_func=self.get_foo)



    def handle_invalid_usage(self,error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response
    
    def get_foo(self):
        raise InvalidUsage('This view is gone', status_code=410)

