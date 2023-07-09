from django.contrib import admin
from .models import Wallet


class WalletAdmin(admin.ModelAdmin):
    list_display = ('wallet_name', 'currency', 'initial_balance', 'date')

admin.site.register(Wallet, WalletAdmin)