from flask_wtf import FlaskForm as Form
from wtforms import StringField
from wtforms import Label
from wtforms import SubmitField
from wtforms import PasswordField,SelectField,HiddenField
from wtforms.validators import DataRequired,EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(Form):
    username = StringField("用户名", validators=[DataRequired()],)
    password = PasswordField("密码", validators=[DataRequired()])
    submit = SubmitField("提交")


class AddForm(Form):
    username = StringField("用户名", validators=[DataRequired()])
    email = StringField("邮箱",validators=[DataRequired()])
    password = PasswordField("密码", validators=[DataRequired(), EqualTo("password2",message="密码不匹配")])
    password2 = PasswordField("确认密码")
    role = SelectField("角色", validators=[DataRequired()], coerce=int)
    submit = SubmitField("提交")

    def validate_username(self,filed):
        if User.query.filter_by(username=filed.data).first() is not None:
            raise ValidationError("用户名已存在")

    def validate_email(self,filed):
        if User.query.filter_by(email=filed.data).first() is not None:
            raise ValidationError("邮箱已存在")


class RegisterForm(Form):
    username = StringField("用户名", validators=[DataRequired()])
    email = StringField("邮箱",validators=[DataRequired()])
    password = PasswordField("密码", validators=[DataRequired(), EqualTo("password2",message="密码不匹配")])
    password2 = PasswordField("确认密码", validators=[DataRequired(), ])
    submit = SubmitField("提交")

    def validate_username(self,filed):
        if User.query.filter_by(username=filed.data).first() is not None:
            raise ValidationError("用户名已存在")

    def validate_email(self,filed):
        if User.query.filter_by(email=filed.data).first() is not None:
            raise ValidationError("邮箱已存在")


class EditForm(Form):
    username = StringField("用户名", validators=[DataRequired()])
    email = StringField("邮箱",validators=[DataRequired()])
    password = PasswordField("密码", validators=[DataRequired(), EqualTo("password2", message="密码不匹配")])
    password2 = PasswordField("确认密码", validators=[DataRequired(), ])
    role = SelectField("角色", coerce=int)
    submit = SubmitField("提交")

    def __init__(self, user, *args, **kwargs):
        super(EditForm, self).__init__(*args, *kwargs)
        self.user = user

    def validate_username(self, filed):
        query = User.query.filter_by(username=filed.data).all()
        if query is not None:
            for x in query:
                if x.id != self.user.id:
                    raise ValidationError("用户名已存在")

    def validate_email(self, filed):
        query = User.query.filter_by(email=filed.data).all()
        if query is not None:
            for x in query:
                if x.id != self.user.id:
                    raise ValidationError("邮箱已存在")