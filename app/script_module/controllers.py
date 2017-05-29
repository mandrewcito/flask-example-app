"""
Blueprint - modules, request - querystring
"""
from flask import Blueprint,request

script_module = Blueprint('script_module',__name__,url_prefix='/script_module')

hello = lambda x: "hello, {0}!".format(x)

@script_module.route('/url/<name>',methods=['GET'])
def url(name):
    """
    url: parameter/url/[a name]
    """
    return hello(name)

@script_module.route('/query',methods=['GET'])
def query_string():
    """
    url: parameter/query?name=[a name]
    """
    name = request.args.get('name')
    return hello(name)

@script_module.route('/body',methods=['POST'])
def body():    
    """
    url: parameter/body
    content-type: application/x-www-form-urlencoded
    variable = name , value = [a name]
    """
    name = request.form['name']
    return hello(name)
