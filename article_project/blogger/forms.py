from django.contrib.auth.models import User
from django import forms
from .models import Blogger


class UserSignupForm(forms.ModelForm):
    class Meta:
        form = User()
        fields = ['email', 'password','username']