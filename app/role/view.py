from . import role
from flask import  request, g, url_for, redirect, render_template, session
from flask_login import login_required
from flask import flash
from ..models import Role
from ..common import get_nav
from .Form import RoleForm
from .. import db
from ..decorators import admin_require


@role.before_request
def init():
    g.nav = get_nav("user")
    g.category = "用户管理"


@role.route("/role_lists")
@admin_require
def role_lists():
    page = request.args.get("page", 1, type=int)
    pagination = Role.query.paginate(page,per_page=10,error_out=False)
    return  render_template("role/role_lists.html", pagination=pagination, title="角色列表")


@role.route("/role_add", methods=["POST", "GET"])
@admin_require
def role_add():
    form = RoleForm()
    if form.validate_on_submit():
        role = Role(name=form.name.data,desc=form.desc.data)
        db.session.add(role)
        flash("角色添加成功", "role")
        return redirect(url_for("role.role_lists"))
    return render_template("role/role_add.html", form=form, title="角色添加")


