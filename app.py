from petfax import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)  # Turn off debug mode in production

# New route
@app.route('/pets')
def pets():
    return 'These are our pets available for adoption!'
