from django.db import models

# Create your models here.
class Wallet(models.Model):

    CURRENCIES = [
        ('US Dollars', 'USD'),
        ('Euro', 'EUR'),
        ('Ghana Cedis', 'GHC'),
        ('GB Pounds', 'GBP'),
        ('Naira', 'NGN'),
        ('Japanese Yen', 'JPY'),
        ('Indian Rupee', 'INR'),
    ]

    wallet_name = models.CharField(max_length=100)
    currency = models.CharField(max_length=20, choices=CURRENCIES)
    initial_balance = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(max_length=400)
    

    def __str__(self):
        return str(self.wallet_name)
