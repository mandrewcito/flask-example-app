
from flask import Blueprint

module2 = Blueprint('module2',__name__,url_prefix='/module2')

@module2.route('/hello',methods=['GET','POST'])
def hello():
    return "[2] Hello, world!"

