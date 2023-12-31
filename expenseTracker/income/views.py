import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Income
from .forms import IncomeForm

from django.core.files.storage import default_storage
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from users.models import Profile
from django.db.models import Q





# @login_required(login_url='login')
# def incomeView(request):
#     user = request.user
#     if user.is_authenticated:
#         profile = Profile.objects.get(user=user)
#         context = {
#             'profile': profile,
#         }
#         return render(request, 'incomepage.html', context)
#     else:
#         return redirect('login')


# CREATE
'''
@login_required
def add_income(request):
    if request.method == "POST":
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            messages.success(request, 'Income added successfully')
            return redirect('income_list') 
    else:
        form = IncomeForm()
    return render(request, 'add_income.html', {'form': form})

# READ
@login_required
def income_list(request):
    incomes = Income.objects.filter(user=request.user)
    return render(request, 'income_list.html', {'incomes': incomes})

# UPDATE
@login_required
def edit_income(request, id):
    income = get_object_or_404(Income, id=id, user=request.user)
    if request.method == "POST":
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            messages.success(request, 'Income updated successfully')
            return redirect('income_list') 
    else:
        form = IncomeForm(instance=income)
    return render(request, 'edit_income.html', {'form': form})

# DELETE
@login_required
def delete_income(request, id):
    income = get_object_or_404(Income, id=id, user=request.user)
    if request.method == "POST":
        income.delete()
        messages.success(request, 'Income deleted successfully')
        return redirect('income_list')
    return render(request, 'confirm_delete.html', {'object': income})

'''
