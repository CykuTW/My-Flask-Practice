from flask import Blueprint, request
from flask.views import View, MethodView


blueprint = Blueprint('index', __name__)


class NormalView(View):
    methods = ['GET']

    def dispatch_request(self):
        if request.method == 'GET':
            return '<h1>Hello, world</h1><h2>With View</h2>'


class ApiView(MethodView):

    def get(self):
        return '<h1>Hello, world</h1><h2>With MethodView</h2>'


blueprint.add_url_rule('/normal', view_func=NormalView.as_view(NormalView.__name__))
blueprint.add_url_rule('/api', view_func=ApiView.as_view(ApiView.__name__))
