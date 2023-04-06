from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

app.app_context().push()

@app.route('/')
def home():
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/pets/<pet_name>/<int:pet_id>', methods=['GET', 'POST'])
def pet(pet_name, pet_id):
    form = PetForm()
    pet = Pet.query.get(pet_id)

    if form.validate_on_submit():
        name = form.pet_name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        return redirect(f'/pets/{name}/{pet.id}')
    else:
        return render_template('pet.html', form=form, pet=pet)