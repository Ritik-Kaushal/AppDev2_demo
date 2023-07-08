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
    SECURITY_PASSWORD_HASH = os.getenv('SECURITY_PASSWORD_HASH') # Hashing Algorithm
    SECURITY_PASSWORD_SALT = os.getenv('SECURITY_PASSWORD_SALT') # Used for hashing passwords
    
    ##### Flask JWT Config #####
    JWT_TOKEN_LOCATION = ["headers"]
    
class ProductionConfig(Config):
    """
    Class for some common configurations of the Flask App related to Production.
    """

    ###### Database Config #####
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')

    ##### Flask Security Config #####
    SECRET_KEY = os.getenv('SECRET_KEY') # Used for token generation
    SECURITY_PASSWORD_HASH = os.getenv('SECURITY_PASSWORD_HASH') # Hashing Algorithm
    SECURITY_PASSWORD_SALT = os.getenv('SECURITY_PASSWORD_SALT') # Used for hashing passwords
    
    ##### Flask JWT Config #####
    JWT_TOKEN_LOCATION = ["headers"]


