from app import db
from datetime import datetime
from flask_login import UserMixin
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(200))
    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Rescuee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(64))
    number = db.Column(db.Integer)
    long = db.Column(db.Float)
    lat = db.Column(db.Float)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))