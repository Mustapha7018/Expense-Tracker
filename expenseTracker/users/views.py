from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
#from . models import Profile
from django.db.models import Q
from .forms import CustomUserCreationForm



# Create your views here.

# USER LOGIN
def loginUser(request):
    #page = 'login'
    #if request.user.is_authenticated:
       # return redirect('dashboard')

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
    
    return render(request, 'login.html')


@login_required(login_url='login')
def dashboard(request):
    user = request.user
    if user:
        return render(request, 'dashboard.html')
    else:
        return redirect('login')


@login_required(login_url='login')
def usersGroup(request):
    return render(request, 'usergroup.html')

@login_required(login_url='login')
def incomeView(request):
    return render(request, 'incomepage.html')

# USER LOGOUT
def logOut(request):
    logout(request)
    return redirect('login')
    messages.info(request, 'User was logged out')


# REGISTER USER
def registerUser(request):
    if request.method == 'POST':
        full_name = request.POST["full_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        Confirm_password = request.POST["confirm_password"]

        if (password != Confirm_password):
            messages.error(request, 'Password Mismatch!')
            return redirect(request.META.get('HTTP_REFERER'))

        try:
            user = User.objects.create_user(username=email, first_name=full_name,password=password)
            user.save()
            messages.success(request, 'User account was created successfully!')
            return redirect('dashboard')
        except:
            messages.error(request, 'An error occurred while creating the user account.')
            return redirect(request.META.get('HTTP_REFERER'))

       
    return render(request, 'signup.html')