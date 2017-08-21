from flask import Response,jsonify

class DefaultResponse(Response):
    charset = 'utf-8'
    default_status = 200
    default_mimetype = ' application/json'

    @classmethod
    def force_type(cls, rv  , environ=None):
        if isinstance(rv, dict):
            rv = jsonify(rv)
        return super(DefaultResponse, cls).force_type(rv, environ)
