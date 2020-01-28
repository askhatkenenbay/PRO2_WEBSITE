from django.shortcuts import render, redirect
from main.models import Person
from .models import CourseTaken
from django.contrib.auth.decorators import login_required, user_passes_test
from users.forms import PersonUpdateForm
from django.contrib import messages
from .forms import CourseRegisterForm, TheoryRegisterForm, TheoryTaskRegisterForm, TheoryGraphicRegisterForm, TheoryFormulaRegisterForm, TheoryLawRegisterForm 
from .models import Course
from django.core.mail import send_mail
from django.conf import settings


user_teacher_required = user_passes_test(lambda user: user.person_type, login_url='/')
def active_teacher_required(view_func):
    decorated_view_func = login_required(user_teacher_required(view_func))
    return decorated_view_func
paid_student_required = user_passes_test(lambda user: user.is_paid, login_url='/')
def active_student_required(view_func):
    decorated_view_func = login_required(paid_student_required(view_func))
    return decorated_view_func

def home(request):
    if request.method == 'POST':
        email_from = settings.EMAIL_HOST_USER
        user_email = request.POST.get('user_email', None)
        if request.POST.get('user_field', None) != None :
            subject = 'Teacher'
            message = 'User Name: '+request.POST.get('user_name', None)+'\nUser Email: '+request.POST.get('user_email', None)+'\nUser Phone: '+request.POST.get('user_phone', None)+'\nUser Field: '+request.POST.get('user_field', None)
        else :
            subject = 'Submission'
            message = 'User Name: '+request.POST.get('user_name', None)+'\nUser Email: '+request.POST.get('user_email', None)+'\nUser Phone: '+request.POST.get('user_phone', None)
        recipient_list = ['pro2edtech@gmail.com',]
        send_mail( subject, message, email_from, recipient_list )
        # ------------------------------------------
        subject = 'Pro2EdTech'
        message = 'You have submitted the application at www.pro2edtech.com, our personal will contact you as soon as possible. \nThis message is auto-sent by the system of www.pro2edtech.com'
        recipient_list = [request.POST.get('user_email', None),]
        send_mail( subject, message, email_from, recipient_list )
        messages.success(request, f'sent')
        return redirect('main-home')
    context = {
        'posts':Person.objects.all()
    }
    return render(request, 'main/home.html',context)    

@login_required
def personal_page(request):
    if request.POST.get('delete', None) != None :
        Person.objects.filter(email=request.user.email).first().delete()
        messages.success(request, f'Your account deleted')
        return redirect('main-home')
    if request.method == 'POST':
        p_form = PersonUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user)
        if p_form.is_valid():
            p_form.save() 
            messages.success(request, f'Your account has been updated!')
            return redirect('main-personal_page')
    else:
        courses = CourseTaken.objects.filter(user_email = request.user.email)
        p_form = PersonUpdateForm(instance=request.user)
    context = {
        'p_form' : p_form ,
        'courses' : courses
    }
    return render(request, 'main/personal.html', context)

@login_required
@active_student_required
def theory(request):
    return render(request, 'main/theory.html')
    
@login_required
@active_student_required
def practice(request):
    return render(request, 'main/practice.html')

@login_required
@active_student_required
def homework(request):
    return render(request, 'main/homework.html')

@login_required
@active_student_required
def test(request):
    return render(request, 'main/test.html')

@login_required
@active_student_required
def formula(request):
    return render(request, 'main/formula.html')

@login_required
@active_student_required
def homeworkNext(request):
    return render(request, 'main/homeworkNext.html')


@login_required
@active_teacher_required
def create_course(request):
    if request.method == 'POST':
        form = CourseRegisterForm(request.POST)
        if form.is_valid():
            request.session['course_name'] = form.cleaned_data['name']
            request.session['person_id'] = form.cleaned_data['creator_email']
            form.save()
            messages.success(request, f'You created course, now create theory')
            return redirect('create-theory')
    else:
        form = CourseRegisterForm()
    return render(request,'main/create_course.html', { 'form' : form })

@login_required
@active_teacher_required
def create_theory(request):
    if request.method == 'POST':
        form = TheoryRegisterForm(request.POST)
        if form.is_valid():
            request.session['theory_name'] = form.cleaned_data['theory_name']
            form.cleaned_data['creator_email'] = request.session.get('person_id')
            form.cleaned_data['course_name'] = request.session.get('course_name')
            form.save()
            messages.success(request, f'You created theory')
            return redirect('create-theory-task')
    else:
        form = TheoryRegisterForm()
    return render(request,'main/create-theory.html', { 'form' : form })


@login_required
@active_teacher_required
def create_theory_task(request):
    if request.method == 'POST':
        form = TheoryTaskRegisterForm(request.POST)
        if form.is_valid():
            form.cleaned_data['creator_email'] = request.session.get('person_id')
            form.cleaned_data['course_name'] = request.session.get('course_name')
            form.cleaned_data['theory_name'] = request.session.get('theory_name')
            form.save()
            messages.success(request, f'You created theory-task')
            return redirect('create-theory-task')
    else:
        form = TheoryTaskRegisterForm()
    return render(request,'main/create-theory-task.html', { 'form' : form })

@login_required
@active_teacher_required
def create_theory_graphic(request):
    if request.method == 'POST':
        form = TheoryGraphicRegisterForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.cleaned_data['creator_email'] = request.session.get('person_id')
            form.cleaned_data['course_name'] = request.session.get('course_name')
            form.cleaned_data['theory_name'] = request.session.get('theory_name')
            form.save()
            messages.success(request, f'You created theory-graphic')
            return redirect('create-theory-graphic')
    else:
        form = TheoryGraphicRegisterForm()
    return render(request,'main/create-theory-graphic.html', { 'form' : form })

@login_required
@active_teacher_required
def create_theory_formula(request):
    if request.method == 'POST':
        form = TheoryFormulaRegisterForm(request.POST)
        if form.is_valid():
            form.cleaned_data['creator_email'] = request.session.get('person_id')
            form.cleaned_data['course_name'] = request.session.get('course_name')
            form.cleaned_data['theory_name'] = request.session.get('theory_name')
            form.save()
            messages.success(request, f'You created theory-formula')
            return redirect('create-theory-formula')
    else:
        form = TheoryFormulaRegisterForm()
    return render(request,'main/create-theory-formula.html', { 'form' : form })

@login_required
@active_teacher_required
def create_theory_law(request):
    if request.method == 'POST':
        form = TheoryLawRegisterForm(request.POST)
        if form.is_valid():
            form.cleaned_data['creator_email'] = request.session.get('person_id')
            form.cleaned_data['course_name'] = request.session.get('course_name')
            form.cleaned_data['theory_name'] = request.session.get('theory_name')
            form.save()
            messages.success(request, f'You created theory-law')
            return redirect('create-theory-law')
    else:
        form = TheoryLawRegisterForm()
    return render(request,'main/create-theory-law.html', { 'form' : form })

@login_required
@active_teacher_required
def my_courses(request):
    context = {
        'courses' : Course.objects.filter(creator_email=request.user.email)
    }
    return render(request,'main/my-courses.html', context)

def courses(request):
    context = {
        'courses' : Course.objects.all()
    }
    return render(request,'main/courses.html', context)

def course_my(request):
    return render(request,'main/courses.html', context)
