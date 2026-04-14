from django.shortcuts import get_object_or_404, redirect, render

from .forms import AccountForm
from .models import Account


def account_list(request):
    accounts = Account.objects.all()
    return render(request, "bank/list.html", {"accounts": accounts})


def add_account(request):
    form = AccountForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("account_list")
    return render(request, "bank/form.html", {"form": form})


def update_account(request, id):
    account = get_object_or_404(Account, id=id)
    form = AccountForm(request.POST or None, instance=account)
    if form.is_valid():
        form.save()
        return redirect("account_list")
    return render(request, "bank/form.html", {"form": form})


def delete_account(request, id):
    account = get_object_or_404(Account, id=id)
    account.delete()
    return redirect("account_list")


def deposit(request, id):
    account = get_object_or_404(Account, id=id)
    account.balance += 1000
    account.save()
    return redirect("account_list")


def withdraw(request, id):
    account = get_object_or_404(Account, id=id)
    account.balance -= 500
    account.save()
    return redirect("account_list")
