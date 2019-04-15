from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from dataloader.settings import Settings

db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app(config_class=Settings):
    app = Flask(__name__)
    app.config.from_object(Settings)
    db.init_app(app)
    bcrypt.init_app(app)

    return app