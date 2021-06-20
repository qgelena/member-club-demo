# Member club

A very simple "Member club" web application, using Flask, SQLAlchemy and Jinja.

## Models:

- Member

## Views

* Додавання члена в клуб
  
* Перегляд головної сторінки з інформацією про членів клубу

## Requirements:

Python >= 3.6.9

## Розгортання і запуск:

### створити venv 
```
$ python3 -m virtualenv -- venv
$ source venv/bin/activate
```

### поставити requirements
```
(venv)$ pip install -r requirements.txt
```

### запуск
```
(venv)$ ./app.py
Listening on http://127.0.0.1:5000
```

### Deployment

* `Dockerfile` and `docker-compose.yml`

* Heroku link here

### test using Pytest:
```
(venv)$ pip install -r test-requirements.txt
(venv)$ pytest
```

