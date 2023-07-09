from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Wallet
from .forms import WalletForm

# Create your views here.
@login_required
def add_wallet(request):
    if request.method == "POST":
        form = WalletForm(request.POST)
        if form.is_valid():
            wallet = form.save(commit=False)
            wallet.save()
            messages.success(request, 'Wallet added successfully')
            return redirect('wallet_list')
    else:
        form = WalletForm()
    return render(request, 'add_wallet.html', {'form': form})

@login_required
def wallet_list(request):
    wallets = Wallet.objects.all()
    return render(request, 'wallet_list.html', {'wallets': wallets})

@login_required
def edit_wallet(request, id):
    wallet = get_object_or_404(Wallet, id=id)
    if request.method == "POST":
        form = WalletForm(request.POST, instance=wallet)
        if form.is_valid():
            form.save()
            messages.success(request, 'Wallet updated successfully')
            return redirect('wallet_list')
    else:
        form = WalletForm(instance=wallet)
    return render(request, 'edit_wallet.html', {'form': form})

@login_required
def delete_wallet(request, id):
    wallet = get_object_or_404(Wallet, id=id)
    if request.method == "POST":
        wallet.delete()
        messages.success(request, 'Wallet deleted successfully')
        return redirect('wallet_list')
    return render(request, 'confirm_delete.html', {'object': wallet})

