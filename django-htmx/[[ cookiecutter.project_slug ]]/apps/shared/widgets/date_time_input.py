from django.forms.widgets import DateTimeInput


class DateTimeFieldInput(DateTimeInput):
    input_type = 'datetime-local'
    default_attrs = {'class': 'nes-input'}

    def __init__(self, attrs=None):
        super().__init__(self.default_attrs if attrs is None else attrs)