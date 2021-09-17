# Django-1
This is a Django Blog application. Users can create accounts, login and make posts.

# To run this Project
* Run Locally
Install a local virtual environment(venv) python3 -m venv env.
Activate the venv - source env/bin/activate.
Install pipenv (pip install pipenv) (pipenv is used for a better dependeny managament.
Install dependencies from pipfile - pipenv install.

# Re-create environment variables
* This should be in the .env file in the root directory
SECRET_KEY
DEBUG
* To generate secret keys you could use this in a terminal window "openssl rand -base64 64"
