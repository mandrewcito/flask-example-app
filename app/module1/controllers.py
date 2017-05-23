from flask import Blueprint

#module1 = Blueprint('module1',__name__,url_prefix='/module1')

#@module1.route('/hello',methods=['GET','POST'])
#def hello():
#    return "hello, world!"

class MyModule(Blueprint):
    def __init__(self):
        super(MyModule,self).__init__("module",__name__,url_prefix='/module1')
        self.add_url_rule("/hello",view_func=self.hello,methods=['GET'])

    def hello(self):
        return "hello,world"
