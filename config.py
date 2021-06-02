################################################
# Config file. 
################################################

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG = False
    TESTING = False
    ENV = ''
    # get some environment variables (don't put secret keys in )
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # PARAM 1 = ....
    # PARAM 2 = ....

class DevelopmentConfig(Config):
    ENV = 'dev'
    DEBUG = True
    DATABASE_URI = os.environ.get('DEV_DATABASE_URL')

class TestingConfig(Config):
    ENV = 'test'
    TESTING = True
    DATABASE_URI = os.environ.get('TEST_DATABASE_URL')

class ProductionConfig(Config):
    ENV = 'prod'
    DATABASE_URI = os.environ.get('PROD_DATABASE_URL')

class HerokuConfig(Config):
    SSL_REDIRECT = True if os.environ.get('DYNO') else False

    # # log to stderr
    # import logging
    # from logging import StreamHandler
    # file_handler = StreamHandler()
    # file_handler.setLevel(logging.INFO)
    # app.logger.addHandler(file_handler)