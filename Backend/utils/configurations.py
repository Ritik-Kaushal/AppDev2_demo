import os
from application.config import LocalDevelopmentConfig, ProductionConfig

from instance.app import app
from instance.database import db
from instance.api import api
from flask_jwt_extended import JWTManager
from application.models import User, Role
from flask_cors import CORS
import utils.loadenv
from datetime import timedelta


# --------------- Setting up the flask app --------------- #
def create_app():
    if(os.getenv("ENV","Development")=="Production"):
        print("----- Starting the production development -----")
        app.config.from_object(ProductionConfig) # Configures the ProductionConfig data with the app
    else:
        print("----- Starting the local development -----")
        print(LocalDevelopmentConfig.SQLALCHEMY_DATABASE_URI)
        app.config.from_object(LocalDevelopmentConfig) # Configures the LocalDevelopmentConfig data with the app

    db.init_app(app)
    jwt = JWTManager(app)
    api.init_app(app)
    CORS(app)
    
    app.app_context().push()


# --------------- Setting up the database --------------- #
def initialise_database():
   with app.app_context():
        inspector = db.inspect(db.engine)
        table_names = inspector.get_table_names()

        if not table_names:  # If no tables exist
            db.create_all()
            admin = Role(name = 'ADMIN', description = '')
            user = Role(name = 'USER', description = '')

            db.session.add(admin)
            db.session.add(user)
            db.session.commit()

            print("Database tables created.")
        else:
            print("Database tables already exist.")
