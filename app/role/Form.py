from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import DataRequired


class RoleForm(FlaskForm):
    name = StringField("角色名", validators=[DataRequired()])
    desc = StringField("角色描述", validators=[DataRequired()])
    submit = SubmitField("提交")