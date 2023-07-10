import os
from application.config import LocalDevelopmentConfig

from instance.app import app
from instance.database import db
from instance.api import api
from instance.mail import mail
from flask_jwt_extended import JWTManager
from application.models import User, Role
from flask_cors import CORS
from instance.celery import cel
import utils.loadenv
from datetime import timedelta
from werkzeug.security import generate_password_hash

from pprint import pprint

# --------------- Setting up the flask app --------------- #
def create_app():
    print("----- Starting the local development -----")
    app.config.from_object(LocalDevelopmentConfig) # Configures the LocalDevelopmentConfig data with the app

    # Configuring Celery
    cel.conf.broker_url = app.config["CELERY_BROKER_URL"]
    cel.conf.result_backend = app.config["CELERY_RESULT_BACKEND"]
    cel.conf.enable_utc = app.config["ENABLE_UTC"]
    cel.conf.timezone = app.config["TIMEZONE"]

    class ContextTask(cel.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    cel.Task = ContextTask

    db.init_app(app)
    JWTManager(app)
    api.init_app(app)
    CORS(app)
    mail.init_app(app)
    app.app_context().push()

    return cel


# --------------- Setting up the database --------------- #
def initialise_database():
   with app.app_context():
        inspector = db.inspect(db.engine)
        table_names = inspector.get_table_names()

        if not table_names:  # If no tables exist
            db.create_all()
            adminRole = Role(name = 'ADMIN', description = '')
            userRole = Role(name = 'END_USER', description = '')

            adminUser = User(email="admin@gmail.com",password=generate_password_hash("password"),role="ADMIN",active=True)
            
            db.session.add(adminRole)
            db.session.add(userRole)
            db.session.add(adminUser)

            db.session.commit()

            print("Database tables created.")
        else:
            print("Database tables already exist.")
