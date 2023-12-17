from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
# Various validators that we are using, added to list of validators
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    # We want to protect against null username
    # And username with certain length requirements
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    # We can use the EqualTo validator to make sure password = confirm_password
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
