from utils.configurations import create_app, initialise_database
from instance.app import app
import api
import utils.celery.tasks


cel = create_app()
initialise_database()


if __name__ == '__main__':
    app.run()