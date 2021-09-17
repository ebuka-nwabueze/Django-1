# Django-1
This is a Django Blog application. Users can create accounts, login and make posts.

# Run Project
### Local

* Install a local virtual environment(venv) 
```
python3 -m venv env

```

* Activate the virtual environment 
```
source env/bin/activate.
```
* Install **pipenv.** It is used for a better dependeny managament.
```
pip install pipenv
```

* Install dependencies from pipfile - 

```
pipenv install
```

## Re-create environment variables
* This should be in the .env file in the root directory
> SECRET_KEY = ****

> DEBUG = ***

* To generate secret keys you could use this in a terminal window 
```
openssl rand -base64 64
```
