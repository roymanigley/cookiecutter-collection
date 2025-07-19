from django.forms.widgets import CheckboxInput


class BooleanFieldInput(CheckboxInput):
    template_name = 'widgets/checkbox.html'
    default_attrs = {'class': 'nes-checkbox'}

    def __init__(self, attrs=None):
        super().__init__(self.default_attrs if attrs is None else attrs)
