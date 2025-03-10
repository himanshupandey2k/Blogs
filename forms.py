from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm) :
    userName = StringField('UserName', validators=[DataRequired(), Length(min=4, max=9)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password =  PasswordField('Password', validators=[DataRequired(), Length(min=5, max=9)])
    confirm_Password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('SignUp')

class LoginForm(FlaskForm) :
    email = StringField('Email', validators=[DataRequired(), Email()])
    password =  PasswordField('Password', validators=[DataRequired(), Length(min=5, max=9)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')