from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import Profile

class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(label='Name', max_length=150)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password')
    password2 = forms.CharField(label='Confirm Password')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'full_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['full_name']
        if commit:
            user.save()
            profile = Profile.objects.create(user=user, full_name=user.first_name)
        return user

