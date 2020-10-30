from webapp import WEBAPP
from app.forms import LoginForm
from app.models import User
from flask import render_template, url_for, redirect, flash
from flask_login import current_user, login_user, login_required, logout_user
@WEBAPP.route('/')
def index():
    return render_template('index.html')

@WEBAPP.route('/login', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        redirect(url_for('webapp.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('invalid username/password')
            return redirect(url_for('webapp.index'))
        login_user(user, remember=form.rememberme.data)
    return render_template('login.html', form=form)

@WEBAPP.route('/logout')
def signout():
    logout_user()
    return redirect(url_for('webapp.index'))