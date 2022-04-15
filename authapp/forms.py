import hashlib
import random

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
import django.forms as forms

from authapp.models import Contacts


class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ('username', 'first_name', 'age', 'avatar', 'country', 'sity', 'district')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class ContactsLoginForm(AuthenticationForm):
    class Meta:
        model = Contacts
        fields = ('username', 'password',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ContactsRegisterForm(UserCreationForm):
    class Meta:
        model = Contacts
        fields = ('username', 'first_name', 'password1', 'password2', 'email', 'age', 'avatar', 'country', 'sity',
                  'district', 'gender')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Отказано в регистрации, Вам меньше 18 лет")
        return data

    def save(self):
        user = super().save()
        user.is_active = True # ВЫЯСНИТЬ
        # salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
        # user.activation_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()
        user.save()
        return user
