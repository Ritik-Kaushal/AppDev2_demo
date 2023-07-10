# -------------- IMPORTING THE REQUIRED MODULES --------------- #
import os
import utils.loadenv

# -------------- PATH OF BASE DIRECTORY --------------- #
basedir = os.path.abspath(os.path.dirname(__file__)) # path of the base directory

# -------------- CONFIGURATION CLASSES --------------- #
class Config():
    """
    Base class for some common configurations of the Flask App.
    """

    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False

class LocalDevelopmentConfig(Config):
    """
    Class for some common configurations of the Flask App related to Local Development.
    """

    ##### Flask APP Config #####
    DEBUG = True

    ##### Database Config #####
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')

    ##### Flask Security Config #####
    SECRET_KEY = os.getenv('SECRET_KEY') # Used for token generation
    
    ##### Flask JWT Config #####
    JWT_TOKEN_LOCATION = ["headers"]

    ##### Celery Config #####
    CELERY_BROKER_URL='redis://127.0.0.1:6379',
    CELERY_RESULT_BACKEND='redis://127.0.0.1:6379'
    ENABLE_UTC = False
    TIMEZONE = "Asia/Calcutta"

    ##### Flask Mail Config #####
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = os.getenv('MAIL_PORT')
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')


