from django.forms.widgets import TimeInput


class TimeFieldInput(TimeInput):
    input_type = 'time'
    default_attrs = {'class': 'nes-input'}

    def __init__(self, attrs=None):
        super().__init__(self.default_attrs if attrs is None else attrs)