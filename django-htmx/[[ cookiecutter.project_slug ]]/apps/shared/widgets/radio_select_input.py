from django.forms.widgets import RadioSelect


class RadioSelectInput(RadioSelect):
    template_name = 'widgets/radio.html'
    default_attrs = {'class': 'nes-input'}

    def __init__(self, attrs=None):
        super().__init__(self.default_attrs if attrs is None else attrs)
