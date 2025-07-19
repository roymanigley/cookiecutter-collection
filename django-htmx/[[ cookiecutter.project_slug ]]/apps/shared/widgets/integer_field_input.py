from django.forms.widgets import NumberInput


class IntegerFieldInput(NumberInput):
    template_name = 'widgets/input.html'
    default_attrs = {'class': 'nes-input'}

    def __init__(self, attrs=None):
        attrs = self.default_attrs if attrs is None else attrs
        attrs['step'] = "1"
        super().__init__(attrs)
