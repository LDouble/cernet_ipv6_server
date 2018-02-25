from . import api_1
from .authentication import auth
from ..decorators import admin_require
from flask import request, g
from ..models import User, TV, TVProgram, TVLog, RecommendLog
from .. import db
from .errors import success, bad_request,unauthorized
from flask_login import AnonymousUserMixin
import time
import re


@api_1.route("/register/",methods=["POST"])
def register():
    username = request.form.get("username", None)
    password = request.form.get("password", None)
    if username is None or password is None:
        return bad_request("参数错误")
    info = request.form.get("info", "")
    device = request.form.get("device", "")
    user = User(**dict(username=username, password=password, info=info, device=device))
    db.session.add(user)
    return success("注册成功!请登录")


@api_1.route("/tv_lists/")
def tv_lists():
    d = time.strftime("%Y-%m-%d") # 日期
    t = time.strftime("H:%M") # 时间
    ip = request.remote_addr
    if judge_legal_ip(ip):
        method = 4
    else:
        method = 6
    sql = """
    select * from TV left join tv_program on(TV.name = tv_program.tv_name)
     where TV.type = {} and tv_program.day = '{}' and tv_program.time > '{}'
     GROUP  BY TV.name
    """
    sql =sql.format(method, d, t)
    temp = db.session.execute(sql)
    result = temp.fetchall()
    return success("获取电视列表成功", result)


def judge_legal_ip(one_str):

    compile_ip=re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if compile_ip.match(one_str):
        return True
    else:
        return False


@api_1.route("/tv_program/",methods=["POST", "GET"])
def tv_program():
    tv_name = request.form.get("tv_name")
    day = time.strftime("%Y-%m-%d") # 日期
    result = TVProgram.query.filter_by(day=day, tv_name=tv_name).all()
    return success("获取节目列表成功", result)


@api_1.route("/tv_log/", methods=["POST", "GET"])
@auth.login_required
def tv_log():
    if isinstance(g.current_user, AnonymousUserMixin):
        return unauthorized("未授权")
    else:
        user_id = g.current_user.id
        program = request.form.get("program")
        t = request.form.get("time")
        is_recommend = request.form.get("is_recommend")
        log = TVLog(program=program, time=t, user_id=user_id,
                    is_recommend=is_recommend)
        db.session.add(log)
        return success("添加日志成功")


@api_1.route("/log_lists/")
@auth.login_required
@admin_require
def log_lists():
    data = TVLog.query.all()
    return success("获取日志列表成功", data)


@api_1.route("/recommend_log/")
@auth.login_required
@admin_require
def recommend_log():
    data = recommend_log.query.all()
    return success("获取推荐日志列表成功", data)

