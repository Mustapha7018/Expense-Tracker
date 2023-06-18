from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from . models import Profile
from django.db.models import Q
from .forms import CustomUserCreationForm

# Create your views here.

# USER LOGIN
def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # check if username exists in database
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        # authenticates username & password
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Username or password is incorrect')
    
    return render(request, 'dashboard/dashboard.html')


# USER LOGOUT
def logout(request):
    logout(request)
    messages.info(request, 'User was logged out')


# REGISTER USER
def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User account was created successfully!')

            login(request, user)
            return redirect('dashboard')

        else:
            messages.error(request, 'An error occurred during registration')
            
    context = {'page': page, 'form': form}
    return render(request, 'users/signup.html', context)