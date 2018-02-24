from flask_httpauth import  HTTPBasicAuth
from flask_login import AnonymousUserMixin, user_unauthorized
from ..models import User
from . import api_1
from flask import jsonify,g
from .errors import unauthorized
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username_or_token, password=""):
    if username_or_token == "":
        g.current_user = AnonymousUserMixin()
        return True
    if password == "":
        g.current_user = User.verify_auth_token(username_or_token)
        g.token_used = True
        return g.current_user is not None
    user = User.query.filter_by(username=username_or_token).first()
    if not user:
        return False
    g.current_user = user
    g.token_used = False
    return user.verify_password(password)


@auth.error_handler
def auth_error():
    return unauthorized("未授权")


@api_1.route("/token", methods=["GET"])
@auth.login_required
def get_token():
    if isinstance(g.current_user, AnonymousUserMixin) or g.token_used:
        return unauthorized("未授权")
    else:
        return jsonify({
            "token":g.current_user.generate_auth_token(expiration=3600).decode(),
            "expiration":3600
        })

