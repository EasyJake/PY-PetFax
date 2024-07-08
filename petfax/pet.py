from flask import Blueprint, render_template
import json

bp = Blueprint('pet', __name__)

@bp.route('/')
def index():
    with open('pets.json') as f:
        pets = json.load(f)
    return render_template('index.html', pets=pets)
