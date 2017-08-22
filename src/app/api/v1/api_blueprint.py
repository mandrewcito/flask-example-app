from flask import Blueprint
from my_view import MyViewAPI

class ApiBlueprint(Blueprint):
    def __init__(self):
        super(ApiBlueprint,self).__init__("v1",__name__,url_prefix='/v1')
        myview = MyViewAPI.as_view('my_view')
        self.add_url_rule('/myview/', defaults={'identifier': None},
                 view_func=myview, methods=['GET',])
        self.add_url_rule('/myview/', view_func=myview, methods=['POST',])
        self.add_url_rule('/myview/<int:identifier>', view_func=myview,
                 methods=['GET', 'PUT', 'DELETE'])
