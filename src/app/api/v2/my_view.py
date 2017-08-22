from flask.views import MethodView

class MyViewAPI(MethodView):

    def get(self, identifier):
        if identifier is None:
            return  {"values":[{"hello":"world api v2"}]}
        else:
            return {"hello":"world api v2"}

    def post(self):
        # create a new user
        pass

    def delete(self, user_id):
        # delete a single user
        pass

    def put(self, user_id):
        # update a single user
        pass
