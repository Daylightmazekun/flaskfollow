# -*- coding: utf-8 -*-
from flask_wtf.form import Form
from wtforms.fields.core import StringField, BooleanField, SelectField
from wtforms.fields.simple import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError

from app.models.account import Role, User
from app.models.post import Category


class EditProfileAdminForm(Form):
    email = StringField('Email', validators = [DataRequired(), Length(0, 54), Email(message = "请输入合法的邮箱地址。")])
    username = StringField('用户名', validators = [DataRequired(), Length(0, 64)])
    confirmed = BooleanField("邮箱认证")
    role = SelectField("姓名", validators = [Length(0, 64)])
    name = StringField("真是姓名", validators = [Length(0, 64)])
    about_me = TextAreaField("个人简介")
    submit = SubmitField("提交")
    def __init__(self, user = None, *args, **kwargs):
        super.role.choices = [(role.id, role.name)
                              for role in Role.query.order_by(Role.id).all()]
        if user:
            self.user = user
        else:
            self.user = None
    def validate_email(self, field):
        guard = False
        if self.user and field.data != self.user.email and User.query.filter_by(email = field.data).first():
            guard = True
        elif not self.user and User.query.filter_by(email = field.data).first():
            guard = True
        if guard:
            raise ValidationError("邮箱地址已经被占用")
    def validate_username(self, field):
        guard = False
        if self.user and field.data != self.user.username and User.query.filter_by(username = field.data).first():
            guard = True
        elif not self.user and User.query.filter_by(username = field.data).first():
            guard = True
        if guard:
            raise ValidationError("用户名已经被占用")
class CategoryForm(Form):
    name = StringField("栏目名称", validators = [DataRequired(), Length(1, 10, message = "太长了.")])
    parent = SelectField("父栏目")
    submit = SubmitField("提交")
    
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        category = Category.query.filter(Category.name == 'None').first()
        choices = [(category.id, category.name)]
        if Category.query.filter(Category.parent_id == 1).count():
            choices.extend([(cg.id, cg.name) for cg in Category.query.filter(Category.parent_id == 1).all() ])          
        self.parent.choices = choices
    def validate_name(self, field):
        if Category.query.filter_by(name = field.data).first():
            raise ValidationError("已经有相同的栏目")
        
        