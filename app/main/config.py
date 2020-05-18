import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_secret_key')
    SECURITY_PASSWORD_SALT = os.getenv('SALT', 'my_secret_key')

    LANGUAGES = {
        'en_EN': 'English',
        'uk_UA': 'Ukrainian',
        'ru_RU': 'Russian'
    }


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig
)
