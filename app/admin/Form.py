from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField
from wtforms import TextAreaField
from wtforms import SubmitField


class SystemForm(FlaskForm):
    site_name = StringField("网站名称")
    email = StringField("站长邮箱")
    site_icp = StringField("备案号")
    site_analytics = TextAreaField("分析代码")
    submit = SubmitField("保存")


class NavForm(FlaskForm):
    name = StringField("名称", validators=[DataRequired()])
    blue = StringField("模块", validators=[DataRequired()])
    method = StringField("方法", validators=[DataRequired()])
    type = StringField("类别")
    submit = SubmitField("添加")


class EditNavForm(FlaskForm):
    name = StringField("名称", validators=[DataRequired()])
    blue = StringField("模块", validators=[DataRequired()])
    method = StringField("方法", validators=[DataRequired()])
    type = StringField("类别")
    submit = SubmitField("保存")

    def __init__(self, nav, *args, **kwargs):
        super(EditNavForm, self).__init__(*args,**kwargs)
        self.nav = nav
