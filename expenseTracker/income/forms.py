from django import forms
from .models import Income

class IncomeForm(forms.ModelForm):
    date = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'placeholder': 'Select a date',
            'type': 'date'
        })
    )

    class Meta:
        model = Income
        fields = ['source', 'currency', 'amount', 'date', 'wallet', 'description']

