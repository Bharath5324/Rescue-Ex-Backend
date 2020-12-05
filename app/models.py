from app import db
from datetime import datetime
from flask_login import UserMixin
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
class Login(UserMixin, db.Model):
    __tablename__ = "Login"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(200))
    role = db.Column(db.Boolean, nullable=False)
    institution = db.relationship('Institution', backref='login', lazy=True)
    user = db.relationship('User', backref='login', lazy=True)
    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Instituion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login_id = db.Column(db.Integer, db.ForeignKey('Login.id'))
    kind = db.Column(db.String(64), nullable = False)
    scanner_id = db.Column(db.String(128), nullable = False, index=True)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login_id = db.Column(db.Integer, db.ForeignKey('Login.id'))
    contact1 = db.Column(db.BigInteger, nullable=False)
    contact2 = db.Column(db.BigInteger, nullable=False)
    contact3 = db.Column(db.BigInteger, nullable=False)
    contact4 = db.Column(db.BigInteger, nullable=False)
    url = db.Column(db.String(128), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    group = db.Column(db.String(20), nullable=False)

@login.user_loader
def load_user(id):
    return Login.query.get(int(id))
    