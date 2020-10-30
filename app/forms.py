from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    rememberme = BooleanField('rememmberme')
    submit = SubmitField('SignIn')