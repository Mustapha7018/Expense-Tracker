from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.registerUser, name='register'),

]