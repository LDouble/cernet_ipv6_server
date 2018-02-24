from flask import Blueprint

user = Blueprint("user", __name__)  # 实例化蓝图

from . import view
