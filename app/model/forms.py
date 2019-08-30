from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    '''
    Default register form
    '''
    username = StringField('username', validators = [DataRequired()])
    password = PasswordField('password', validators=[validators.Required(), validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('confirm', validators = [DataRequired()])