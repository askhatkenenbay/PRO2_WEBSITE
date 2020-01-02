from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm,CustomUserCreationForm
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', { 'form' : form } )





