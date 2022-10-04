class Config(object):
    """
    Common configurations
    """
    # Put any configurations here that are common accross all environments 
    SECRET_KEY = 'zxcvbnm123'
    # SQLALCHEMY_DATBASE_URI = '<use_database>://<username>:<password>@<IP>/<database_name>'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/bodymass'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """
    Development Configurations
    """ 
    DEBUG = True
    SQLALCHEMY_ECHO = True

app_config = {
    'development':DevelopmentConfig
}