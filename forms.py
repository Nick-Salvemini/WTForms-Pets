from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

species_available = ['Dog', 'Cat', 'Ferret', 'Fish', 'Pig', 'Chinchilla']

class PetForm(FlaskForm):
    name = StringField('Pet Name', validators=[InputRequired(message='A Name is Required')])
    species = SelectField('Species', choices=[(sp) for sp in species_available], default='Select a Species')
    photo_url = StringField('Photo_URL', validators=[InputRequired(message='An Image is Required'), URL(require_tld=True, message='Must be a valid URL')])
    age = IntegerField('Age', validators=[InputRequired(message='An Age is Required'), NumberRange(min = 0, max = 40)])
    notes = StringField('Notes', validators=[Optional()])
    available = BooleanField('Are They Available?')