from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,upgrade

app = Flask(__name__)

app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app,db)


from .models import uc_model