from flask import Flask, render_template

# Factory function
def create_app():
    app = Flask(__name__)

    # Index route
    @app.route('/')
    def index(): 
        return render_template('index.html')
    
    # Register pet blueprint 
    from . import pet 
    app.register_blueprint(pet.bp)

    # Register fact blueprint 
    from . import fact
    app.register_blueprint(fact.bp)

    # Error handler for 404 errors
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    # Return the app 
    return app
