from django.shortcuts import render, redirect
from main.models import Person
from django.contrib.auth.decorators import login_required
from users.forms import PersonUpdateForm
from django.contrib import messages

def home(request):
    context = {
        'posts':Person.objects.all()
    }
    return render(request, 'main/home.html',context)    

@login_required
def personal_page(request):
    if request.method == 'POST':
        p_form = PersonUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user)
        if p_form.is_valid():
            p_form.save() 
            messages.success(request, f'Your account has been updated!')
            return redirect('main-personal_page')
    else:
        p_form = PersonUpdateForm(instance=request.user)
    context = {
        'p_form': p_form
    }
    return render(request, 'main/personal.html', context)