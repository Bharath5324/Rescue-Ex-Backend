from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_login import LoginManager

app = Flask (__name__)
login = LoginManager(app)
# login.login_view = 'webapp.routes.signin'
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from app import routes, models
routes.init_app(app)