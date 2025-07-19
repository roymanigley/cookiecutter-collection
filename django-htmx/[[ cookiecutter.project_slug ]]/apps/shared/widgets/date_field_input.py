from django.forms.widgets import DateInput


class DateFieldInput(DateInput):
    input_type = 'date'
    default_attrs = {'class': 'nes-input'}

    def __init__(self, attrs=None):
        super().__init__(self.default_attrs if attrs is None else attrs)