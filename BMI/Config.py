
class Config(object):
    SECRET_KEY="abcde"
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:root@localhost/health_bmi"
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class Development(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO=True
    DEBUG=True


app_config={"development":Development}
