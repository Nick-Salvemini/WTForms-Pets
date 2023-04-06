from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Email, Optional


class PetForm(FlaskForm):
    name = StringField('Pet Name', validators=[InputRequired(message='A Name is Required')])
    species = StringField('Species', validators=[InputRequired(message='A Species is Required')])
    photo_url = StringField('Photo_URL', validators=[InputRequired(message='An Image is Required')])
    age = IntegerField('Age', validators=[InputRequired(message='An Age is Required')])
    notes = StringField('Notes', validators=[Optional()])
    availability = BooleanField('Are They Available?')