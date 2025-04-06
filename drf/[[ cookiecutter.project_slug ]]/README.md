# [[ cookiecutter.project_name ]]

## Setup
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
./manage.py makemigration
./manage.py migrate
./manage.py createsuperuser
```
