import  os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY") or b'\x89\xf0vV\x9f\x8c\x19aX\xa3$\xc3\xd9 \x85C\xb9{\xffV'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:root@localhost/video_server"
    # dialect + driver://username:password@host/database


class TestingConfig(Config):
    pass


class ProductionConfig(Config):
    pass


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}