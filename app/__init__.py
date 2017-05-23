from flask import Flask

from app.module1.controllers import MyModule as m1
from app.module2.controllers import module2 as m2
from app.parameter.controllers import parameter_module as parameter_module

app = Flask(__name__)

#app.config.from_object('config')

#Register modules
app.register_blueprint(m1())
app.register_blueprint(m2)
app.register_blueprint(parameter_module)
