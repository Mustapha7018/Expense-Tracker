from django.urls import path
from . import views

app_name = 'wallet'

urlpatterns = [
    path('add/', views.add_wallet, name='add_wallet'),
    path('list/', views.wallet_list, name='wallet_list'),
    path('edit/<int:id>/', views.edit_wallet, name='edit_wallet'),
    path('delete/<int:id>/', views.delete_wallet, name='delete_wallet'),
]
