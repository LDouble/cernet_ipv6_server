from . import index
from flask import request,abort
from flask import render_template
from ..models import API


@index.route("/")
def index_function():
    api = API.query.all()
    return render_template("index/index.html", api=api, title="IPTV6")


@index.route("/detail/")
def detail():
    id = request.args.get("id")
    if id is None:
        abort(404)
    api = API.query.get(id)
    if api:
        return render_template("index/detail.html", api=api, title="IPTV6<br/> 列表详情")
    else:
        abort(404)