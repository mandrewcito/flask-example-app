from flask import Blueprint

class ClassModule(Blueprint):
    def __init__(self):
        super(ClassModule,self).__init__("class_module",__name__,url_prefix='/class_module')
        self.add_url_rule("/hello",view_func=self.hello,methods=['GET'])

    def hello(self):
        return "hello,world"
