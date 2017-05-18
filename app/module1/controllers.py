from flask import Blueprint

module1 = Blueprint('module1',__name__,url_prefix='/module1')

@module1.route('/hello',methods=['GET','POST'])
def hello():
    return "hello, world!"
