from django.forms.widgets import NumberInput


class FloatFieldInput(NumberInput):
    template_name = 'widgets/input.html'
    default_attrs = {'class': 'nes-input'}

    def __init__(self, attrs=None):
        super().__init__(self.default_attrs if attrs is None else attrs)
