import os

from flask import current_app


class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(current_app.instance_path, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    APP_VERSION = '0.0.1'

    SECRET_KEY = 'not_safe_secret_key'
    SECURITY_PASSWORD_SALT = SECRET_KEY

    SECURITY_PASSWORD_HASH = 'bcrypt'
    SECURITY_LOGIN_USER_TEMPLATE = "security/login_user.jinja2"
    SECURITY_FORGOT_PASSWORD_TEMPLATE = "security/reset_password.jinja2"
    SECURITY_CHANGE_PASSWORD_TEMPLATE = "security/change_password.jinja2"
    SECURITY_RECOVERABLE = True
    SECURITY_CHANGEABLE = True

    EMAIL_FROM = ('', 'flaskdesk@localhost')
    SECURITY_EMAIL_SENDER = EMAIL_FROM

    # MAIL
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 25
    MAIL_USE_SSL = False
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''

    CELERY_BROKER_URL = 'redis://localhost/0'
    CELERY_BACKEND_URL = 'redis://localhost/0'

    REDIS_URL = 'redis://localhost/0'

    {% if cookiecutter.sentry_dsn %}
    SENTRY_USER_ATTRS = ['user_kind', 'email', 'first_name', 'last_name']
    {% endif %}


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{{cookiecutter.app_name}}@127.0.0.1/{{cookiecutter.app_name}}'

    SECRET_KEY = 'REPLACE_ME_WITH_A_RANDOM_STRING_ASAP'
    SECURITY_PASSWORD_SALT = SECRET_KEY

    EMAIL_FROM = ('{{cookiecutter.app_name}}', '{{cookiecutter.app_name}}@localhost')
    SECURITY_EMAIL_SENDER = EMAIL_FROM

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''

    {% if cookiecutter.sentry_dsn %}
    SENTRY_DSN = '{{cookiecutter.sentry_dsn}}'
    {% endif %}


class TestingConfig(BaseConfig):
    pass


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:toor@127.0.0.1/{{cookiecutter.app_name}}'

    DEBUG = True
    TESTING = True  # Suppress Emails
