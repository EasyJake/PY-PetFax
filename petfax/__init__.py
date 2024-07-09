# PY-PETFAX/petfax/__init__.py
                  
from flask import Flask, render_template

# factory
def create_app():
    app = Flask(__name__)

    # index route
    @app.route('/')
    def index(): 
        return render_template('index.html')

    # register pet blueprint 
    from . import pet 
    app.register_blueprint(pet.bp)

   # register fact blueprint 
    from . import fact
    app.register_blueprint(fact.bp)

    # return the app 
    return app