# -*- coding: utf-8 -*-
from flask_wtf.form import Form
from wtforms.fields.core import StringField, SelectField, BooleanField
from wtforms.fields.simple import TextAreaField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length

from app.models.post import Category


def validate_tag(self, field):
    if field.data.find(', ') != -1:
        raise ValidationError('请使用英文半角‘,’来分隔标签、')
class ArtcleForm(Form):
    title = StringField('标题', validators = [DataRequired()])
    summary = TextAreaField('摘要', validators = [DataRequired(), Length(1, 250, message = "too long")])
    tags = StringField('标签', validators = [validate_tag])
    category = SelectField('栏目', coerce = int)
    is_draft = BooleanField("作为草稿")
    submit = SubmitField('提交')
    def __init__(self, *args, **kwargs):
        super(ArtcleForm, self).__init__(*args, **kwargs)
        self.category.choices = [(cg.id. cg.name) for cg in Category.query.all()]
        
        
class CommentForm(Form):
    body = StringField('', validators = [DataRequired(), Length(1, 200, message = "too long")])
    submit = SubmitField('提交')   