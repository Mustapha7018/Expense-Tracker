from django.contrib import admin
from .models import Income

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('source', 'date', 'currency', 'amount', 'wallet')

admin.site.register(Income, IncomeAdmin)

