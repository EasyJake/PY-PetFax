from flask import Flask

def create_app():
    app = Flask(__name__, static_folder='../static')
    
    from .pet import bp as pet_bp
    app.register_blueprint(pet_bp, url_prefix='/pets')
    
    @app.route('/')
    def index():
        return 'Welcome to PetFax!'
    
    return app
