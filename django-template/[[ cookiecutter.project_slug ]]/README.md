# [[ cookiecutter.project_name ]]

## Initialisation
```
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
```

## Run
```
./manage.py runserver
```

## Add / Remove model fields
> When you add, remove or update the model fields you will need to adapt the files in:
- `./apps/core/models/`
- `./apps/core/forms/`
