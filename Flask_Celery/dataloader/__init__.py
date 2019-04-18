from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dataloader.settings import Setting

app = Flask(__name__)
app.config.from_object(Setting)
db = SQLAlchemy(app)

from dataloader.core.routes import core
app.register_blueprint(core)