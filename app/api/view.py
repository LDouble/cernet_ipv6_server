from . import api
from flask import render_template, redirect, url_for
from flask import g,request,flash
from .. import db
from ..common import get_nav
from ..models import API
from .Form import APIForm
from ..decorators import admin_require


@api.before_request
def init():
    g.nav = get_nav("api")
    g.category = "API管理"


@api.route("/api_lists/")
@admin_require
def api_lists():
    page = request.args.get("pag", type=int)
    pagination = API.query.paginate(page, per_page=10,error_out=False)
    return render_template("api/api_lists.html", pagination=pagination, title="API列表")


@api.route("/api_add/", methods=["POST", "GET"])
@admin_require
def api_add():
    form = APIForm()
    if form.validate_on_submit():
        data = form.data
        data.pop("csrf_token")
        data.pop("submit")
        api = API(**data)
        db.session.add(api)
        flash("API添加成功","api")
        return  redirect(url_for("api.api_lists"))
    return render_template("api/api_add.html", form=form, title="API添加")


@api.route("/api_edit/", methods=["POST", "GET"])
@admin_require
def api_edit():
    id = request.args.get("id")
    form = APIForm()
    if form.validate_on_submit():
        data = form.data
        data.pop("csrf_token")
        data.pop("submit")
        api = API(**data)
        db.session.add(api)
        flash("API编辑成功","api")
        return redirect(url_for("api.api_lists"))
    api = API.query.get(id)
    form.method.data =api.method
    form.api.data = api.api
    form.desc.data = api.desc
    form.param.data = api.param
    return render_template("api/api_add.html", form=form, title="API编辑")


@api.route("/api_delete/")
@admin_require
def api_delete():
    id = request.args.get("id")
    api = API.query.get(id)
    if api:
        db.session.delete(api)
        flash("删除API成功", "api")
    else:
        flash("请求错误", "api")
    return redirect(url_for("api.api_lists"))
