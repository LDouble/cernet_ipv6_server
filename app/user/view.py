from . import user
from flask import render_template, redirect, request, url_for,flash
from flask import session, g
from ..models import User
from ..models import Role
from .. import db
from . import Form
from flask_login import login_user, login_required, logout_user, current_user
from ..common import get_nav
from ..decorators import admin_require

@admin_require
def get_role():
    role = [(x.id, x.name) for x in Role.query.all()]
    return role


@user.before_request
def init():
    g.nav = get_nav("user")
    g.category = "用户管理"


@user.route("/user_lists/")
@admin_require
def user_lists():
    page = request.args.get('page', 1, type=int)
    pagination = User.query.paginate(page, per_page=10, error_out=False)
    return render_template("user/user_lists.html", pagination=pagination, title="用户列表")


@user.route("/user_add/", methods=["POST","GET"])
@admin_require
def user_add():
    form = Form.AddForm()
    form.role.choices = get_role()
    if form.validate_on_submit():
        data = form.data
        data.role_id = data.role
        data.pop("role")
        data.pop("submit")
        data.pop("csrf_token")
        data.pop("password2")
        user = User(**data)
        db.session.add(user)
        flash("添加用户成功","user")
        return redirect(url_for("user.user_lists"))
    return render_template("user/user_add.html", title="添加用户", form=form)


@user.route("/user_edit/", methods=["POST","GET"])
@admin_require
def user_edit():
    id = request.args.get("id")
    user = User.query.get_or_404(id)
    form = Form.EditForm(user)
    form.role.choices = get_role()
    if form.validate_on_submit():
        user.username = form.username.data
        user.password = form.password.data
        user.email = form.email.data
        user.role_id = form.role.data
        db.session.add(user)
        flash("编辑用户成功","user")
        return redirect(url_for("user.user_lists"))
    form.username.data = user.username
    form.email.data = user.email
    return render_template("user/user_add.html", title="编辑用户", form=form)


@user.route("/login/", methods=["POST", "GET"])
def login():
    form = Form.LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user is not None and user.verify_password(password):
            login_user(user)
            return redirect(request.args.get("next") or url_for("admin.index"))
        flash("账号或密码错误", "login")
    return render_template("user/login.html", form=form, title="用户登陆")


@user.route("/register/", methods=["POST", "GET"])
def register():
    form = Form.RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    password=form.password.data,
                    email=form.email.data)
        db.session.add(user)
        flash("注册成功","register")
        return redirect(url_for("user.login"))
    return render_template("user/register.html", form=form, title="用户注册")


@user.route("/logout/")
def logout():
    logout_user()
    return redirect(url_for("user.login"))


@user.route("/profile/")
@login_required
def profile():
    return "必须登陆"

