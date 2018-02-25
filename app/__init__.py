from flask_sqlalchemy import SQLAlchemy
from flask import Flask,g
from flask_bootstrap import Bootstrap
from config import config
from flask_login import LoginManager
from flask_pagedown import PageDown
import json

db = SQLAlchemy()
bootstrap = Bootstrap()
pagedown = PageDown()
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "auth.login"
with open("system.cnf") as f:
    scnf = json.loads(f.readline())


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.config["sys_cnf"] = scnf
    db.init_app(app)
    pagedown.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    from .user import user
    from .admin import admin
    from .role import role
    from .tv import tv
    from .api import api
    from .api import api_1
    from .index import index
    app.register_blueprint(user, url_prefix="/user")
    app.register_blueprint(admin, url_prefix="/admin")
    app.register_blueprint(role, url_prefix="/role")
    app.register_blueprint(tv, url_prefix="/tv")
    app.register_blueprint(api, url_prefix="/api")
    app.register_blueprint(api_1, url_prefix="/api/1.0")
    app.register_blueprint(index, url_prefix="")
    from .common import get_nav

    @app.before_request
    def init():
        g.navbar = get_nav("nav")
    return app
