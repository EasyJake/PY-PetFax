# config    
from flask import Flask
app = Flask(__name__)  # This line creates a Flask application instance.

# index route
@app.route('/')        # This decorator specifies that the function below handles requests to the root URL ('/').
def index():           # This defines a function named 'index' which will be called when the root URL is accessed.
    return 'Hello, this is PetFax!'  # The function returns a string when the root URL is accessed.

# pets index route
@app.route('/pets')    # This decorator specifies that the function below handles requests to the '/pets' URL.
def pets():            # This defines a function named 'pets' which will be called when the '/pets' URL is accessed.
    return 'These are our pets available for adoption!'  # The function returns a string when the '/pets' URL is accessed.
