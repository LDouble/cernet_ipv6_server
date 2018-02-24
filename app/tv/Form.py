from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField
from wtforms.validators import DataRequired


class TvForm(FlaskForm):
    url = StringField("流地址", validators=[DataRequired()])
    name = StringField("电视台名称", validators=[DataRequired()])
    type = IntegerField("类别", validators=[DataRequired()])
    submit = SubmitField("提交")

