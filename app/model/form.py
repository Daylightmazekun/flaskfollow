from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired
from flask_mongoengine import validators

class RegisterForm(FlaskFrom):
    '''
    Default register form
    '''
    username = StringField('username', validators = [DataRequired()])
    password = PasswordField('password', validators=[validators.Required(), validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('confirm', validators = [DataRequired()])
