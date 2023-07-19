import datetime
from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from . models import Profile, UserActivity
from django.db.models import Q
from .forms import CustomUserCreationForm



# Create your views here.

# LOGIN USER
def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # check if username exists in database
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'Username does not exist')
            return redirect(request.META.get('HTTP_REFERER'))

        # authenticates username & password
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login success!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Username or password is incorrect')
    
    return render(request, 'login.html')


# DASHBOARD
@login_required(login_url='login')
def dashboard(request):
    user = request.user
    if user.is_authenticated:
        profile = Profile.objects.get(user=user)
        total_users = User.objects.count()
        recent_operations = UserActivity.objects.filter(user=user).order_by('-time')[:10]
        date_stamp = datetime.datetime.now()
        full_name = user.get_full_name()
        context = {
            'profile': profile,
            'total_users': total_users,
            'recent_operations': recent_operations,
            'date_stamp': date_stamp,
            'full_name' : full_name,
        }
        return render(request, 'dashboard.html', context)
    else:
        return redirect('login')



@login_required(login_url='login')
def usersGroup(request):
    user = request.user
    if user.is_authenticated:
        profile = Profile.objects.get(user=user)

        if request.method == 'POST':
            username = request.POST.get('username')
            full_name = request.POST.get('full-name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            user_type = request.POST.get('user-type')
            privileges = request.POST.get('privileges')
            wallet = request.POST.get('wallet')

            # Create a new user
            new_user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            # Update the user's full name
            new_user.profile.full_name = full_name

            # Assign user-type, privileges, and wallet if user is staff/admin
            if user.is_staff:
                new_user.profile.user_type = user_type
                new_user.profile.privileges = privileges
                new_user.profile.wallet = wallet

            new_user.profile.save()

            messages.success(request, 'User added successfully.')

            return redirect('users')

        total_users = User.objects.count()
        users = User.objects.all()
        context = {
            'profile': profile,
            'total_users': total_users,
            'users': users
        }
        return render(request, 'usergroup.html', context)
    else:
        return redirect('login')







@login_required(login_url='login')
def incomeView(request):
    user = request.user
    if user.is_authenticated:
        profile = Profile.objects.get(user=user)
        context = {
            'profile': profile,
        }
        return render(request, 'incomepage.html', context)
    else:
        return redirect('login')


@login_required(login_url='login')
def expenseView(request):
    user = request.user
    if user.is_authenticated:
        profile = Profile.objects.get(user=user)
        context = {
            'profile': profile,
        }
        return render(request, 'expensepage.html', context)
    else:
        return redirect('login')


@login_required(login_url='login')
def walletView(request):
    user = request.user
    if user.is_authenticated:
        profile = Profile.objects.get(user=user)
        context = {
            'profile': profile,
        }
        return render(request, 'walletpage.html', context)
    else:
        return redirect('login')


@login_required(login_url='login')
def settingsView(request):
    user = request.user
    if user.is_authenticated:
        profile = Profile.objects.get(user=user)
        email = user.email
        context = {
            'profile': profile,
            'email' : email,
        }
        return render(request, 'settingspage.html', context)
    else:
        return redirect('login')

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
            user = User.objects.create_user(
                username=email, 
                first_name=full_name.split()[0], 
                last_name=full_name.split()[1] if len(full_name.split()) > 1 else '',
                password=password
            )

            profile, created = Profile.objects.get_or_create(user=user, full_name=full_name)
            if created:
                profile.save()

            authenticated_user = authenticate(username=email, password=password)
            if authenticated_user is not None:
                login(request, authenticated_user)
                messages.success(request, 'User account was created successfully!')
                return redirect('dashboard')
        except Exception as e:
            print(e)  # print the exception for debugging
            messages.error(request, 'An error occurred while creating the user account.')
            return redirect(request.META.get('HTTP_REFERER'))

    return render(request, 'signup.html')




# EDIT USER SETTINGS
@login_required(login_url='login')
def editProfile(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')

        # Checking if profile_image exists in the request
        if 'profile_image' in request.FILES:
            print("Profile image received")
            profile_image = request.FILES['profile_image']
        else:
            print("No profile image received in request")
            profile_image = None

        # Update the user's profile
        profile.full_name = full_name
        if profile_image:
            print("Profile image exists, updating the profile image")
            if profile.profile_image:  # Make sure a profile image exists before deleting it
                print("Existing profile image found, deleting it")
                profile.profile_image.delete(save=False)  # Delete the old profile picture if exists
            profile.profile_image = profile_image
        profile.save()

        # Update the user's email if it has changed
        if email != user.email:
            user.email = email
            user.save()

        # Change the user's password if provided
        if old_password and new_password:
            if user.check_password(old_password):
                user.set_password(new_password)
                user.save()
                # Re-authenticate the user with the new password
                user = authenticate(username=user.username, password=new_password)
                login(request, user)
            else:
                messages.error(request, 'Incorrect old password. Password not changed.')

        messages.success(request, 'Profile updated successfully.')
        return redirect('dashboard')

    context = {
        'profile': profile,
        'user': user,
        'user_type': 'Admin' if user.is_staff else 'User',
        'privileges': 'Edit dashboard' if user.is_staff else 'View dashboard'}

    return render(request, 'settingspage.html', context)







