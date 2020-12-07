from webapp import WEBAPP
from .auth import authorization_required
from flask import render_template
from flask_login import current_user
from app.models import Institution
@WEBAPP.route("/dashboard")
@authorization_required
def dashboard():
    user = Institution.query.filter_by(login_id=current_user.id)
    render_template("dashboard")