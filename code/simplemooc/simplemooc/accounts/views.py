from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.conf import settings

from .forms import RegisterForm

# Create your views here.


def dashboard(request):
    template_name = 'accounts/dashboard.html'
    return render(request, template_name)


def edit(request):
    template_name = 'accounts/edit.html'
    return render(request, template_name)


def edit_password(request):
    template_name = 'accounts/edit_password.html'
    return render(request, template_name)


def register(request):
    template_name = 'accounts/register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=user.username,
                password=form.cleaned_data['password1']
            )
            login(request, user)
            return redirect('core:home')
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)


def logout(request):
    template_name = 'accounts/logout.html'
    return render(request, template_name)
