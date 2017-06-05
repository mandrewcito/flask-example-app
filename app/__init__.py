from flask import Flask,jsonify

from app.class_module.controllers import ClassModule as ClassModule
from app.script_module.controllers import script_module as script_module

from app.errors.invalid_usage import InvalidUsage as InvalidUsage

from app.responses.default import DefaultResponse

app = Flask(__name__)

# Default response register

app.response_class = DefaultResponse

# Register modules as a class instance 
app.register_blueprint(ClassModule())

# Register modules as an instantiated object
app.register_blueprint(script_module)

# Register custom errors
@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@app.route('/error/custom/foo')
def get_foo():
    raise InvalidUsage('This view is gone', status_code=410)


