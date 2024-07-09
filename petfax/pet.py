# PY-PETFAX/petfax/pet.py

from flask import Blueprint, render_template
import json

# Load the pet data from JSON
with open('pets.json') as file:
    pets = json.load(file)

# Create a Blueprint for 'pet' which will handle all pet-related routes
bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def index():
    """ Render the index page showing all pets. """
    return render_template('index.html', pets=pets)

@bp.route('/<int:pet_id>')
def show(pet_id):
    """ Render a page showing details for a specific pet. """
    if 1 <= pet_id <= len(pets):
        pet = pets[pet_id - 1]  # Adjust for zero-indexing
        return render_template('show_pet.html', pet=pet)
    else:
        return render_template('404.html'), 404  # Return a custom 404 page if the pet is not found


