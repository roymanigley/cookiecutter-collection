from django.forms.widgets import Textarea


class TextFieldInput(Textarea):
    template_name = 'widgets/textarea.html'
    default_attrs = {'class': 'nes-textarea'}

    def __init__(self, attrs=None):
        super().__init__(self.default_attrs if attrs is None else attrs)
