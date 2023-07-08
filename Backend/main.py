from utils.configurations import create_app, initialise_database
from instance.app import app
import api

if __name__ == '__main__':
    create_app()
    initialise_database()

    app.run()