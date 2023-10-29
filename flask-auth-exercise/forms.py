from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class FeedbackForm(FlaskForm):
    title = StringField("Title", validators=[
        DataRequired(),
        Length(min=5, max=100, message="Title must be between 5 and 100 characters")
    ])
    content = TextAreaField("Content", validators=[
        DataRequired(),
        Length(min=20, message="Content must be at least 20 characters long")
    ])
    submit = SubmitField("Submit Feedback")