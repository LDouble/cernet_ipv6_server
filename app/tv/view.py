from . import tv
from flask import render_template, request, g
from flask import redirect, url_for,flash
from ..models import TV, TVProgram, TVLog, RecommendLog
from .Form import TvForm
from .. import db
from ..common import get_nav
from ..decorators import admin_require


@tv.before_request
def init():
    g.nav = get_nav("tv")
    g.category = "电视管理"


@tv.route("/tv_lists/")
@admin_require
def tv_lists():
    page = request.args.get("page", type=int)
    pagination = TV.query.paginate(page, per_page=10, error_out=False)
    return render_template("tv/tv_lists.html", pagination=pagination,title="电视列表")


@tv.route("/tv_add/", methods=["POST","GET"])
@admin_require
def tv_add():
    form = TvForm()
    if form.validate_on_submit():
        tv = TV(url=form.url.data,
                name=form.name.data,
                type=form.type.data)
        db.session.add(tv)
        flash("电视台增加成功","tv")
        return redirect(url_for("tv.tv_lists"))
    return render_template("tv/tv_add.html", form=form, title="电视增加")


@tv.route("/tv_program/")
@admin_require
def tv_program():
    page = request.args.get("page", type=int)
    pagination = TVProgram.query.paginate(page, per_page=10, error_out=False)
    return render_template("tv/tv_program.html", pagination=pagination, title="节目列表")


@tv.route("/tv_log/")
@admin_require
def tv_log():
    page = request.args.get("page", type=int)
    pagination = TVLog.query.paginate(page, per_page=10, error_out=False)
    return render_template("tv/tv_log.html", pagination=pagination, title="日志列表")


@tv.route("/recommend_log/")
@admin_require
def recommend_log():
    page = request.args.get("page", type=int)
    pagination = RecommendLog.query.paginate(page, per_page=10, error_out=False)
    return render_template("tv/recommend_log.html", pagination=pagination, title="节目推荐日志")

