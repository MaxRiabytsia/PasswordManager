from django import forms
from .models import Password

import random
import string


def generate_password():
    password_length = 16
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = "".join(random.sample(chars, password_length))
    return password


class PasswordForm(forms.ModelForm):
    password = forms.CharField(initial=generate_password)

    class Meta:
        model = Password
        exclude = ('service_icon_url', 'service_name', 'date_created', 'last_modified', 'author')
