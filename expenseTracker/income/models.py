from django.db import models
from wallet.models import Wallet

class Income(models.Model):
    INCOME_SOURCES = [
        ('SALES', 'Sales'),
        ('LICENSING & ROYALTIES', 'Licensing & Royalties'),
        ('SERVICE FEES', 'Services Fees'),
        ('RENTAL INCOME', 'Rental Income'),
        ('COMMISSION INCOME', 'Commmission Income'),
        ('INVESTMENT INCOME', 'Investment Income'),
        ('DIVIDEND', 'Dividend'),
    ]

    CURRENCIES = [
        ('US Dollars', 'USD'),
        ('Euro', 'EUR'),
        ('Ghana Cedis', 'GHC'),
        ('GB Pounds', 'GBP'),
        ('Naira', 'NGN'),
        ('Japanese Yen', 'JPY'),
        ('Indian Rupee', 'INR'),
    ]

    source = models.CharField(max_length=50, choices=INCOME_SOURCES)
    currency = models.CharField(max_length=20, choices=CURRENCIES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    description = models.TextField(max_length=400)

    def save(self, *args, **kwargs):
        # If this income instance already exists and is being updated
        if self.pk:
            # Subtract the old amount from the wallet's balance before adding the new one
            old_income = Income.objects.get(pk=self.pk)
            self.wallet.balance -= old_income.amount

        self.wallet.balance += self.amount
        self.wallet.save()
        super(Income, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.wallet.balance -= self.amount
        self.wallet.save()
        super(Income, self).delete(*args, **kwargs)

    def __str__(self):
        return self.get_source_display()
