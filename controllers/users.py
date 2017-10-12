from flask import Blueprint, request, render_template, escape, abort
from flask.views import View, MethodView


blueprint = Blueprint('users', __name__)


class LoginView(MethodView):
    
    def get(self):
        return render_template('users/login.html')
    
    def post(self):
        if all(key in request.form for key in ('username', 'password')):
            return escape(request.form['username'])
        else:
            abort(400)


blueprint.add_url_rule('/login', view_func=LoginView.as_view(LoginView.__name__))
