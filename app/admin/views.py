from . import admin
from ..decorators import admin_require
from flask import render_template
from .Form import SystemForm, NavForm, EditNavForm
from flask import current_app
from flask import flash,url_for,g
from flask import request,redirect
from ..models import Nav
from .. import db
from ..common import get_nav
import json


@admin.before_request
def init():
    g.nav = get_nav("admin")
    g.category = "系统管理"


@admin.route("/")
@admin_require
def index():
    return redirect(url_for("admin.system"))


@admin.route("/system/", methods=["POST", "GET"])
@admin_require
def system():
    config = current_app.config
    form = SystemForm(**config["sys_cnf"])
    if form.validate_on_submit():
        info = {"site_name": form.site_name.data,
                "email": form.email.data,
                "site_analytics": form.site_analytics.data,
                "site_icp": form.site_icp.data
                }
        current_app.config.update(sys_cnf=info)
        with open("system.cnf", "w") as f:
            f.write(json.dumps(info))
        flash("系统配置更新成功", "update_system")
    return render_template("admin/system.html", form=form, title="网站设置")


@admin.route("/nav_lists/", methods=["POST", "GET"])
@admin_require
def nav_lists():
    page = request.args.get('page', 1, type=int)
    pagination = Nav.query.order_by(Nav.id.desc()).paginate(page, per_page=10, error_out=False)
    return render_template("admin/nav_lists.html", pagination=pagination, title="导航列表")


@admin.route("/nav_add/", methods=["POST", "GET"])
@admin_require
def nav_add():
    form = NavForm()
    if form.validate_on_submit():
        data = form.data
        data.pop("submit")
        data.pop("csrf_token")
        nav = Nav(**data)
        db.session.add(nav)
        flash("添加导航成功", "nav")
        return redirect(url_for("admin.nav_lists"))
    return render_template("admin/nav_add.html", form=form, title="导航添加")


@admin.route("/nav_delete/",)
@admin_require
def nav_delete():
    id = request.args.get("id")
    if id:
        nav = Nav.query.filter_by(id=id).first()
        if nav:
            db.session.delete(nav)
            flash("删除导航成功", "nav")
        else:
            flash("删除导航失败", "nav")
    else:
        flash("参数错误", "nav")
    return redirect(url_for("admin.nav_lists"))


@admin.route("/nav_edit/", methods=["POST", "GET"])
@admin_require
def nav_edit():
    id = request.args.get("id")
    nav = Nav.query.get_or_404(id)
    form = EditNavForm(nav)
    if form.validate_on_submit():
        nav.name = form.name.data
        nav.blue = form.blue.data
        nav.method = form.method.data
        nav.type = form.type.data
        db.session.add(nav)
        flash("编辑成功", "nav")
        return redirect(url_for("admin.nav_lists"))
    form.name.data = nav.name
    form.blue.data = nav.blue
    form.method.data = nav.method
    form.type.data = nav.type
    form.submit.default = "保存"
    return render_template("admin/nav_add.html", form=form, title="导航编辑")
