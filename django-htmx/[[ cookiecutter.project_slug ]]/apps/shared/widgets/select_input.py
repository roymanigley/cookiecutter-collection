from django.forms.widgets import Select


class SelectInput(Select):
    template_name = 'widgets/select.html'
    default_attrs = {'class': 'nes-input'}

    def __init__(self, attrs=None):
        super().__init__(self.default_attrs if attrs is None else attrs)
