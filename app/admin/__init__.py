# -*- coding:utf-8 -*-
# 管理蓝图
from flask import Blueprint
admin = Blueprint("admin",__name__)

from . import views