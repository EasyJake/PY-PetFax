
# PetFax

PetFax is a simple Flask-based web application that provides information about pets. Users can view a list of pets, see details about individual pets, and submit fun facts about pets.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Data Sources](#data-sources)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features
- View a list of pets with names and photos.
- View detailed information about individual pets.
- Submit new fun facts about pets.

## Installation

### Prerequisites
- Python 3.x
- Flask

### Setup
1. **Clone the repository:**
   ```sh
   git clone https://github.com/EasyJake/PY-PetFax.git
   cd petfax
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python3 -m venv venv
   . venv/bin/activate
   ```

3. **Install Flask and other dependencies:**
   ```sh
   pip install Flask
   python3 -m pip install --upgrade pip
   ```

## Usage
1. **Activate the virtual environment:**
   ```sh
   . venv/bin/activate
   ```

2. **Run the app:**
   ```sh
   flask run --reload
   ```

3. **Access the application:**
   Open your web browser and navigate to `http://127.0.0.1:5000`.


## Data Sources
- **Dog Photo**: Karseten Winegeart on Unsplash
- **Cat Photo**: Alvan Nee on Unsplash
- **Rabbit Photo**: Emiliano Vittoriosi on Unsplash


## Contributing
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License
This project is licensed under the MIT License.

## Acknowledgements
- [Flask](https://flask.palletsprojects.com/)
- [Unsplash](https://unsplash.com/) for the photos
