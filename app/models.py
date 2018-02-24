from . import db
from . import login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import  current_app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(125), unique=True)
    desc = db.Column(db.String(125))
    users = db.relationship("User", backref="role")


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, index=True)
    email = db.Column(db.String(255),unique=True, index=True)
    password_hash = db.Column(db.String(255))
    ip = db.Column(db.String(255))
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))
    device = db.Column(db.String(255))  # 设备型号，
    info = db.Column(db.String(255))  # 个人信息，用于分类

    def generate_auth_token(self, expiration):
        s = Serializer(current_app.config["SECRET_KEY"], expires_in=expiration)
        return s.dumps(dict(id=self.id))

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            data = s.loads(token)
        except:
            return None
        return User.query.get(data['id'])


    @property
    def password(self):
        raise AttributeError("Password can not be read")

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User {}>".format(self.username)


class Nav(db.Model):
    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    name = db.Column(db.String(255))
    blue = db.Column(db.String(255))
    method = db.Column(db.String(255))
    type = db.Column(db.String(255), default="nav")


class TV(db.Model):  #电视台
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    url = db.Column(db.String(512))
    name = db.Column(db.String(512))
    type = db.Column(db.SmallInteger)  # 4 或者 6


class TVProgram(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    program_name = db.Column(db.String(255),unique=True)
    tv_name = db.Column(db.String(255))  # 电视台
    time = db.Column(db.String(255))  # 时间段
    day = db.Column(db.String(255))  # 哪一天
    type = db.Column(db.String(255))  # 节目的类型


class TVLog(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    program = db.Column(db.String(255))  # 时间节目、电视台
    user_id =db.Column(db.Integer)


class RecommendLog(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(512))
    user_id = db.Column(db.Integer)  # 电视用户id
    feedback = db.Column(db.Integer)  # 是否观看，观看了多久


class API(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    api = db.Column(db.String(255))
    method = db.Column(db.String(24))
    desc = db.Column(db.String(512))
    param = db.Column(db.Text)
