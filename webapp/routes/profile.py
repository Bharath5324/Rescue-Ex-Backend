from webapp import WEBAPP
from .auth import authorization_required
from flask import render_template
from flask_login import current_user
from app.models import Institution, User
from app.firebase import fire
@WEBAPP.route("/dashboard")
@authorization_required
def dashboard():
    institute = Institution.query.filter_by(login_id=current_user.id).first()
    print(current_user.id)
    user = User.query.filter_by
    dashdat = fire("readerid", institute.scanner_id)
    return render_template("dashboard.html", institute=institute, user=user, dashdat=dashdat)