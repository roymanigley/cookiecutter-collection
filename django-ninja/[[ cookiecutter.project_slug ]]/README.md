# [[ cookiecutter.project_name ]]

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
./manage.py makemigration
./manage.py migrate
./manage.py createsuperuser
```

## Add an endpoint to Controller

```python
from ninja_extra import route
from ninja_extra.searching import searching, Searching
from ninja_extra.ordering import ordering, Ordering
from ninja.pagination import paginate


@route.get('test', response={200: list[DummyRetreiveSchema]})
@paginate()
@ordering(Ordering, ordering_fields=['-name']) # needs to be below @paginate()
@searching(Searching, search_fields=['name']) # needs to be below @paginate()
def get_test(self):
    return self.service.get_all()
```