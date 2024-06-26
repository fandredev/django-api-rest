## Stack used

<img src="https://skillicons.dev/icons?i=python,django,githubactions,postgresql&theme=dark" />


**Lint:** Black

**CI/CD:** Github Actions

## Authors
- [@fandredev](https://www.linkedin.com/in/devfandre/)
- [Alura](https://cursos.alura.com.br/formacao-django-rest)

<br>

# Installation:
## First, clone this repository.
```bash
git clone git@github.com:fandredev/django-api-rest.git
```

## Create virtual environment with Python

```bash
python -m venv venv
```
## OR
```bash
python3 -m venv venv
```

## Activate the virtual environment

```bash
source venv/bin/activate
```

## Install dependencies using pip
```bash
pip install -r requirements.txt
```

- Look the .env.example file to change your informations from PostgreSQL database. 
A database must be created using PostgreSQL manually and your server needs be a running in other terminal.

In example, i use asdf to instance postgres in my machine. (https://asdf-vm.com/)

![image](https://github.com/fandredev/django-api-rest/assets/49297012/ff27b012-8189-4410-819b-520301a7f4ce)
![image](https://github.com/fandredev/django-api-rest/assets/49297012/fde61b22-bc75-4b82-8aae-f7153c8dd200)



## Run migrations to database
```bash
python manage.py migrate
```

## Create a superuser
```bash
python manage.py createsuperuser
```
    
## Run development server
```bash
python manage.py runserver
```
- or using ```launch.json```  file (if you use vscode)

## Run tests
```bash
python manage.py test
```

## Open Django Admin
<h4>
In another tab, open browser and put http://localhost:8000/control in URL browser. Log in with your superuser</h4>
<br>

## OPTIONAL (Populate your database using faker data)

```
python populate_students.py && python populate_courses.py
``` 

## Use collection
<h4>Use DRF.postman_collection.json file to use Django Rest Framework routes</h4>

![Screenshot from 2024-05-18 17-58-06](https://github.com/fandredev/django-api-rest/assets/49297012/6d51ea14-f39c-48fa-9602-de3bbf994eb9)


- Pass, the user and password authorization to using routes (super/password that were created with ```python manage.py createsuperuser```)
<br>

![image](https://github.com/fandredev/django-api-rest/assets/49297012/0fa811c5-020d-44a9-a7c9-3351420c3beb)

- by default, the answers will come in .xml; Change this using 'Accept' header with 'application/json' value.
![Screenshot from 2024-05-22 19-12-41](https://github.com/fandredev/django-api-rest/assets/49297012/69969618-9888-4876-be17-40316acdf48f)

- Note: to use students routes v2 use, http://localhost:8000/students?version=v2
<br>


## Feedback

If you have any feedback, please let us know via profissionalf.andre@gmail.com

## Referencies

 - [Django documentation](https://docs.djangoproject.com/en/5.0/)
 - [Python](https://www.python.org/)
 - [Black formatter](https://black.readthedocs.io/en/stable/the_black_code_style/index.html)
 - [Alura Training](https://cursos.alura.com.br/formacao-django-rest)
