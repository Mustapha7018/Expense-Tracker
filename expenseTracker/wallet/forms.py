from django import forms
from .models import Wallet

class WalletForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = ['wallet_name', 'currency', 'initial_balance', 'date', 'description']
