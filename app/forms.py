from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length, Optional


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class SearchForm(FlaskForm):
    cuisine = SelectField('cuisine', choices=[
        ('surprise', 'Surprise Me!'),
        ('italian', 'Italian'),
        ('Mexican', 'Mexican'),
        ('chinese', 'Chinese'),
        ('Indo-Chinese', 'Indo-Chinese'),
        ('american', 'American'),
        ('Indian', 'Indian'),
        ('japanese', 'Japanese'),
        ('Turkish', 'Turkish'),
        ('International', 'International'),
        ('european', 'European'),
        ('Eastern European', 'Eastern European'),
        ('bar', 'Bar'),
        ('dessert', 'Dessert'),
        ('Greek', 'Greek'),
        ('Yemeni', 'Yemeni'),
        ('Brazilian', 'Brazilian'),
        ('Canadian', 'Canadian'),
        ('Thai', 'Thai'),
        ('French', 'French'),
        ('Australian', 'Australian'),

    ], validators=[Optional()])

    budget = SelectField('budget', choices=[
        ('surprise', 'Surprise Me!'),
        ('under_150', 'Under 150'),
        ('150_250', '150-250'),
        ('over_250', 'Over 250')
    ], validators=[Optional()])

    vibe = SelectField('vibe', choices=[
        ('surprise', 'Surprise Me!'),
        ('relaxed', 'Relaxed'),
        ('casual', 'Casual'),
        ('family', 'Family'),
        ('aesthetic', 'Aesthetic'),
        ('smart', 'Smart'),
        ('bar', 'Bar'),
        ('late', 'Late'),
        ('entertainment', 'Entertainment'),
        ('romantic', 'Romantic'),
        ('fine dining', 'Fine Dining'),
        ('dark', 'Dark'),
    ], validators=[Optional()])

    submit = SubmitField('Find Restaurants')