import models
import validators
from flask import Blueprint, request, render_template, escape, abort, session
from flask.views import View, MethodView
from flask_validate import validate
from utils import bcrypt


blueprint = Blueprint('users', __name__)


class LoginView(MethodView):
    
    def get(self):
        return render_template('users/login.html')
    
    @validate(validators.users.LoginValidator())
    def post(self):
        username = request.form['username']
        password = request.form['password']
        user = models.User.query.filter_by(username=username).first()
        if bcrypt.check_password_hash(user.password, password):
            session['id'] = user.id
            session['username'] = user.username
            return '<h1>Hi, {}</h1>'.format(escape(username))
        return '<h1>The username or password was incorrect.</h1>'


class ProfileView(MethodView):

    def get(self):
        return ''


blueprint.add_url_rule('/login', view_func=LoginView.as_view(LoginView.__name__))
blueprint.add_url_rule('/profile', view_func=ProfileView.as_view(ProfileView.__name__))
