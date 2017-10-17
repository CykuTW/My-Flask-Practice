from flask import request
from wtforms import Form, StringField
from wtforms.validators import DataRequired, Length


class LoginValidator(object):
    class InnerValidator(Form):
        username = StringField('username', validators=[DataRequired(), Length(5, 20)])
        password = StringField('password', validators=[DataRequired(), Length(5, 20)])

    def validate(self):
        validator = LoginValidator.InnerValidator(request.form)
        return validator.validate()
