# -*- coding: utf-8 -*-
from flask_wtf.form import Form
from wtforms.fields.core import StringField
from wtforms.fields.simple import TextAreaField, SubmitField
from wtforms.validators import Length, DataRequired


class EditProfileForm(Form):
    name = StringField("真事姓名", validators = [Length(0, 64)])
    location = StringField("居住地", validators = [Length(0, 64)])
    about_me = TextAreaField("个人简介")
    submit = SubmitField("提交")
    
    
class ChatForm(Form):
    content = StringField('', validators = [DataRequired(), Length(1, 200, message = "Too long")])
    submit = SubmitField("发送")