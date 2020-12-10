from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField
class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    rememberme = BooleanField('Remember Me')
    submit = SubmitField('SignIn')

class InstituteSignupForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    kind = StringField('Institution Type', validators=[DataRequired()])
    scanner_id = StringField('Scanner I.D', validators=[DataRequired()])