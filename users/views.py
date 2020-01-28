from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm,CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.conf import settings

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email_from = settings.EMAIL_HOST_USER
            subject = 'Submission'
            user_name = form.cleaned_data['name']
            user_email = form.cleaned_data['email']
            user_phone = form.cleaned_data['phone']
            message = 'User Name: '+user_name+'\nUser Email: '+user_email+'\nUser Phone: '+user_phone
            recipient_list = ['pro2edtech@gmail.com',]
            send_mail( subject, message, email_from, recipient_list )
            # -------------------------------------------
            subject = 'Pro2EdTech'
            message = 'You have registered at www.pro2edtech.com, our personal will contact you as soon as possible. \nThis message is auto-sent by the system of www.pro2edtech.com'
            recipient_list = [user_email,]
            send_mail( subject, message, email_from, recipient_list )
            # ----------------------------------------------
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', { 'form' : form } )





