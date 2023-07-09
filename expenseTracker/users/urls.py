from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logOut, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('users/', views.usersGroup, name='users'),

]