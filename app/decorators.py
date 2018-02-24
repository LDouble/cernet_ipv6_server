# -*- coding:utf-8 -*-
from functools import wraps
from flask_login import current_user,AnonymousUserMixin
from flask import abort


def admin_require(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):

        if current_user.is_anonymous or (current_user.role and current_user.role.id < 2):
            abort(403)
        return f(*args, **kwargs)
    return decorated_function

