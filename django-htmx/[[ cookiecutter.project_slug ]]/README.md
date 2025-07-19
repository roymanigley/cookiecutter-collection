# [[ cookiecutter.project_name ]]

## Initial steps
```bash
git init && git add . && git commit -m "initial commit"
python -m venv .venv
source .venv/bin/activate (Unix)
./venv/Scripts/activate (Windows)
pip install -r requirements.txt
git init
git add .
git commit -m"Initial commit"
```

## Define/Redefine your models
```bash
python manage.py cookiecutter
```

## Regenerate the project
> you have to commit all your changes before you can regenerate
```bash
git add .
git commit -m"Defined the models"
python manage.py cookiecutter_run
```

## Apply the migrations
```bash
./manage.py makemigration
./manage.py migrate
```

## Apply the translations
```bash
./manage.py makemessages -l en
./manage.py makemessages -l de
./manage.py makemessages -l fr
./manage.py compilemessages
```

## Create a superuser
```bash
./manage.py createsuperuser
./manage.py runserver
```

## Create run the server
```bash
./manage.py runserver
```