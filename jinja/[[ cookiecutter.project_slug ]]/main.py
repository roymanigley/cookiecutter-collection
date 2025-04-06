from jinja2 import FileSystemLoader, Environment
from typing import Optional


def uppercase_filter(value) -> Optional[str]:
    if isinstance(value, str):
        return value.upper()
    return value


loader = FileSystemLoader("templates")
env = Environment(loader=loader)
env.filters['uppercase'] = uppercase_filter

template = env.get_template('template.txt')

text = template.render(
    {'name': 'Jinja'}
)

print(text)
