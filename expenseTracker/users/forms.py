from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(label='Name', max_length=150)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password')
    password2 = forms.CharField(label='Confirm Password')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['full_name', 'email', 'password1', 'password2']
