from wtforms import Form, TextField
from wtforms.validators import Length, DataRequired


class LoginValidation(Form):
    username = TextField('username', [DataRequired(), Length(5, 20)])
    password = TextField('password', [DataRequired(), Length(5, 20)])