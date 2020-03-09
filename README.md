# shortener

## Installation

This project requires Python 3.7 and Django 2.2.11

The recommended way to install this project is to use Pipenv. The included Pipfile will set up a virtual environment with Python 3.7.x and Django 2.2.11

```
$ pipenv shell
$ pipenv install
```

Alternatively you can use the provided requirements.txt file to install Django with pip.

```pip install -r requirements.txt```


## Setup 

Then you have to setup a database in your project. 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
```
Migrate 
```
$ cd src
$ python manage.py migrate
```
Create superuser 
```
$ python manage.py createsuperuser
```
Now you are ready to start the application:

```
$ python manage.py runserver
```

By default local host name http://localhost:8000/ in settings 
```
HOST_NAME = 'http://localhost:8000/'
```

