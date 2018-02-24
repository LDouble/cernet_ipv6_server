from flask_wtf import  FlaskForm
from wtforms import StringField
from wtforms import SubmitField,TextAreaField
from wtforms.validators import DataRequired


class APIForm(FlaskForm):
    api = StringField("API地址", validators=[DataRequired()])
    method = StringField("请求类型", validators=[DataRequired()])
    desc = StringField("描述",validators=[DataRequired()])
    param = TextAreaField("参数说明",validators=[DataRequired()])
    submit = SubmitField("提交")