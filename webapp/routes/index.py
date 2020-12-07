from webapp import WEBAPP
from app.models import User
from flask import render_template, url_for, redirect, flash
from flask_login import current_user, login_user, login_required, logout_user
@WEBAPP.route('/')
def index():
    return render_template('index.html')