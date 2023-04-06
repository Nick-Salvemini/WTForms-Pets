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
    
    pet = Pet.query.get(pet_id)
    form = PetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data

        db.session.commit()
        name = pet.name
        id = pet.id
        return redirect(f'/pets/{name}/{id}')
    else:
        return render_template('pet.html', form=form, pet=pet)
    
@app.route('/delete/<int:pet_id>')
def delete_pet(pet_id):
    pet = Pet.query.get(pet_id)
    db.session.delete(pet)
    db.session.commit()
    return redirect('/')

@app.route('/new_pet', methods=['GET', 'POST'])
def add_pet():
    form = PetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        availability = form.availability.data

        new_pet = Pet(name=name, species=species, phot_url=photo_url, age=age, notes=notes, availability=availability)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('new_pet.html', form=form)