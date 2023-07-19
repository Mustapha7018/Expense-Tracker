from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logOut, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('users/', views.usersGroup, name='users'),
    path('income/', views.incomeView, name='income'),
    path('expense/', views.expenseView, name='expenses'),
    path('wallet/', views.walletView, name='wallets'),
    path('settings/', views.settingsView, name='settings'),

    path('settings/edit/', views.editProfile, name='edit-profile'),


]