import re

from cookiecutter.utils import simple_filter


def _snake_case(value):
    text = re.sub(r'[\s-]+', '_', value)
    text = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', text)
    return text.lower()


@simple_filter
def snake_case(value: str) -> str:
    return _snake_case(value)


@simple_filter
def kebab_case(value: str) -> str:
    return _snake_case(value).replace('_', '-')


@simple_filter
def as_model_field(field_name: str, field_values: dict) -> str:
    model_field = field_name
    field_type = field_values['type']
    attributes = field_values['attributes']
    nullable = not attributes['required']
    if field_type == 'Relationship':
        on_delete = 'CASCADE' if attributes['cascade'] else 'DO_NOTHING'
        model_field += f' = models.ForeignKey(\'{attributes["relation"]}\', on_delete=models.{on_delete}, null={nullable})'
    elif field_type == 'ChoicesField':
        choices_class = field_name.title().replace('_', '')
        choices_fields = '\n        '.join(
            [f'{c} = \'{c}\'' for c in attributes['choices']])
        model_field += f' = models.CharField(null={nullable}, choices={choices_class}.choices, max_length=255)'
        model_field = f'''
    class {choices_class}(models.Choices):
        {choices_fields}
    
    {model_field}
    '''
    elif field_type == 'CharField':
        model_field += f' = models.CharField(max_length={attributes["max_length"]}, null={nullable})'
    elif field_type == 'FileField':
        model_field += f' = models.FileField(upload_to=\'{attributes["upload_to"]}\', null={nullable})'
    else:
        model_field += f' = models.{field_type}(null={nullable})'

    return model_field
