from django.contrib.auth.forms import AuthenticationForm

from mainapp.models import Contact


class ContactLoginForm(AuthenticationForm):
    class Meta:
        model = Contact
        fields = ('username', 'password',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
