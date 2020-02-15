from django.shortcuts import render, redirect
from main.models import Person
from .models import *
from django.contrib.auth.decorators import login_required, user_passes_test
from users.forms import PersonUpdateForm
from django.contrib import messages
from .forms import CourseRegisterForm, TheoryRegisterForm, TheoryTaskRegisterForm, TheoryGraphicRegisterForm, TheoryFormulaRegisterForm, TheoryLawRegisterForm, HomeworkForm, HomeworkPointsForm
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

temp_god_required = user_passes_test(lambda user: user.is_god, login_url='/')
def god_required(view_func):
    decorated_view_func = login_required(temp_god_required(view_func))
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
    theory = Theory.objects.filter(course_name = request.session.get('curr_course') )
    context = {
        'theory' : theory
    }
    return render(request, 'main/theory.html',context)
    
@login_required
@active_student_required
def practice(request):
    cur_theory = request.GET.get('theory', '')
    request.session['curr_theory'] = cur_theory
    theory = Theory.objects.filter(course_name = request.session.get('curr_course'), theory_name = cur_theory )
    theory_task = TheoryTask.objects.filter(theory_name = cur_theory)
    theory_law = TheoryLaw.objects.filter(theory_name = cur_theory)
    theory_graphic =TheoryGraphic.objects.filter(theory_name = cur_theory)
    context = {
        'theory' : theory,
        'task' : theory_task,
        'law' : theory_law,
        'graphic' : theory_graphic
    }
    return render(request, 'main/practice.html',context)

@login_required
@active_student_required
def homework(request):
    curr_course = request.session.get('curr_course')
    hw = Homework.objects.filter(course_name = curr_course, is_optional=False)
    op = Homework.objects.filter(course_name = curr_course,is_optional=True)
    context = {
        'homework' : hw,
        'optional' : op
    }
    return render(request, 'main/homework.html',context)

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
    cur_hw = request.GET.get('homework', '')
    curr_course = request.session.get('curr_course')
    hw = Homework.objects.filter(course_name = curr_course, homework_name = cur_hw)
    points = HomeworkPoints.objects.filter(course_name = curr_course, homework_name = cur_hw)
    context = {
        'homework' : hw,
        'points' : points
    }
    return render(request, 'main/homeworkNext.html',context)


@login_required
@god_required
def create_course(request):
    if request.method == 'POST':
        form = CourseRegisterForm(request.POST)
        if form.is_valid():
            request.session['course_name'] = form.cleaned_data['name']
            request.session['person_id'] = form.cleaned_data['creator_email']
            # form.save()
            temp = Course(name=form.cleaned_data['name'],course_type=form.cleaned_data['course_type'],creator_email=form.cleaned_data['creator_email'])
            temp.save()
            messages.success(request, f'You created course, now create theory')
            return redirect('create-theory')
    else:
        form = CourseRegisterForm()
    return render(request,'main/create_course.html', { 'form' : form })

@login_required
@god_required
def create_theory(request):
    if request.method == 'POST':
        form = TheoryRegisterForm(request.POST)
        if form.is_valid():
            request.session['theory_name'] = form.cleaned_data['theory_name']
            form.cleaned_data['creator_email'] = request.session.get('person_id')
            form.cleaned_data['course_name'] = request.session.get('course_name')
            # form.save()
            temp = Theory(creator_email=form.cleaned_data['creator_email'],course_name=form.cleaned_data['course_name'],theory_name=form.cleaned_data['theory_name'],order=form.cleaned_data['order'])
            temp.save()
            messages.success(request, f'You created theory')
            return redirect('create-theory-task')
    else:
        form = TheoryRegisterForm()
    return render(request,'main/create-theory.html', { 'form' : form })


@login_required
@god_required
def create_theory_task(request):
    if request.method == 'POST':
        form = TheoryTaskRegisterForm(request.POST)
        if form.is_valid():
            form.cleaned_data['creator_email'] = request.session.get('person_id')
            form.cleaned_data['course_name'] = request.session.get('course_name')
            form.cleaned_data['theory_name'] = request.session.get('theory_name')
            # form.save()
            temp = TheoryTask(creator_email=form.cleaned_data['creator_email'],course_name=form.cleaned_data['course_name'],theory_name=form.cleaned_data['theory_name'],task_type=form.cleaned_data['task_type'],task=form.cleaned_data['task'])
            temp.save()
            messages.success(request, f'You created theory-task')
            return redirect('create-theory-task')
    else:
        form = TheoryTaskRegisterForm()
    return render(request,'main/create-theory-task.html', { 'form' : form })

@login_required
@god_required
def create_theory_graphic(request):
    if request.method == 'POST':
        form = TheoryGraphicRegisterForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.cleaned_data['creator_email'] = request.session.get('person_id')
            form.cleaned_data['course_name'] = request.session.get('course_name')
            form.cleaned_data['theory_name'] = request.session.get('theory_name')
            # form.save()
            temp=TheoryGraphic(creator_email=form.cleaned_data['creator_email'],course_name=form.cleaned_data['course_name'],theory_name=form.cleaned_data['theory_name'],order=form.cleaned_data['order'],graphic=form.cleaned_data['image'])
            temp.save()
            messages.success(request, f'You created theory-graphic')
            return redirect('create-theory-graphic')
    else:
        form = TheoryGraphicRegisterForm()
    return render(request,'main/create-theory-graphic.html', { 'form' : form })

@login_required
@god_required
def create_theory_formula(request):
    if request.method == 'POST':
        form = TheoryFormulaRegisterForm(request.POST)
        if form.is_valid():
            form.cleaned_data['creator_email'] = request.session.get('person_id')
            form.cleaned_data['course_name'] = request.session.get('course_name')
            form.cleaned_data['theory_name'] = request.session.get('theory_name')
            # form.save()
            temp = TheoryFormula(creator_email=form.cleaned_data['creator_email'],course_name=form.cleaned_data['course_name'],theory_name=form.cleaned_data['theory_name'],header=form.cleaned_data['header'],main=form.cleaned_data['main'],footer=form.cleaned_data['footer'],category=form.cleaned_data['category'])
            temp.save()
            messages.success(request, f'You created theory-formula')
            return redirect('create-theory-formula')
    else:
        form = TheoryFormulaRegisterForm()
    return render(request,'main/create-theory-formula.html', { 'form' : form })

@login_required
@god_required
def create_theory_law(request):
    if request.method == 'POST':
        form = TheoryLawRegisterForm(request.POST)
        if form.is_valid():
            form.cleaned_data['creator_email'] = request.session.get('person_id')
            form.cleaned_data['course_name'] = request.session.get('course_name')
            form.cleaned_data['theory_name'] = request.session.get('theory_name')
            # form.save()
            temp = TheoryLaw(creator_email=form.cleaned_data['creator_email'],course_name=form.cleaned_data['course_name'],theory_name=form.cleaned_data['theory_name'],name=form.cleaned_data['name'],text=form.cleaned_data['text'],more=form.cleaned_data['more'])
            temp.save()
            messages.success(request, f'You created theory-law')
            return redirect('create-theory-law')
    else:
        form = TheoryLawRegisterForm()
    return render(request,'main/create-theory-law.html', { 'form' : form })

@login_required
@active_teacher_required
def create_homework(request):
    if request.method == 'POST':
        form = HomeworkForm(request.POST)
        if form.is_valid():
            form.cleaned_data['creator_email'] = request.session.get('person_id')
            form.cleaned_data['course_name'] = request.session.get('course_name')
            request.session['homework'] = form.cleaned_data['name']
            # form.save()
            if request.user.person_type:
                temp = Homework(creator_email=request.user.email,course_name=request.session.get('curr_course'),order=form.cleaned_data['order'],homework_name=form.cleaned_data['name'],text=form.cleaned_data['text'],is_optional=True)
            else:
                temp = Homework(creator_email=form.cleaned_data['creator_email'],course_name=form.cleaned_data['course_name'],order=form.cleaned_data['order'],homework_name=form.cleaned_data['name'],text=form.cleaned_data['text'],is_optional=False) 
            temp.save()
            messages.success(request, f'You created homework')
            return redirect('create-homework-points')
    else:
        form = HomeworkForm()
    return render(request,'main/create-homework.html', { 'form' : form })

@login_required
@active_teacher_required
def create_homework_points(request):
    if request.method == 'POST':
        form = HomeworkPointsForm(request.POST)
        if form.is_valid():
            form.cleaned_data['creator_email'] = request.session.get('person_id')
            form.cleaned_data['course_name'] = request.session.get('course_name')
            form.cleaned_data['homework_name'] = request.session.get('homework')
            # form.save()
            temp = HomeworkPoints(creator_email=form.cleaned_data['creator_email'],course_name=form.cleaned_data['course_name'],homework_name=form.cleaned_data['homework_name'],points=form.cleaned_data['point'])
            temp.save()
            messages.success(request, f'You created homework-point')
            return redirect('create-homework-points')
    else:
        form = HomeworkPointsForm()
    return render(request,'main/create-homework-points.html', { 'form' : form })


# @login_required
# def my_courses(request):
#     context = {
#         'courses' : Course.objects.filter(creator_email=request.user.email)
#     }
#     return render(request,'main/my-courses.html', context)


def courses(request):
    context = {
        'courses' : Course.objects.all()
    }
    return render(request,'main/courses.html', context)

@login_required
def course_my(request): 
    request.session['curr_course'] = request.GET.get('value', '')
    context = {
        'course_name' : request.GET.get('value', ''),
    }
    return render(request,'main/special.html', context)

def chemistry(request):
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
        return redirect('main/temp/physics.html')
    return render(request,'main/temp/chemistry.html')
def physics(request):
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
        return redirect('main/temp/physics.html')
    return render(request,'main/temp/physics.html')
def math(request):
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
        return redirect('main/temp/physics.html')
    return render(request,'main//temp/math.html')

@active_student_required
def survey(request):
    if request.method == 'POST':
        goal = request.POST.get('user_goal', None)
        client = request.POST.get('user_client', None)
        name = request.POST.get('user_name', None)
        subject = request.POST.get('user_subject', None)
        money = request.POST.get('user_money', None)
        email = request.user.email
        temp = SurveyStudent(student_name = name, client_name=client,goal=goal,subject=subject,money=money,email=email)
        temp.save()
        messages.success(request, f'done')
        return redirect('survey')
    temp = SurveyStudent.objects.latest()
    context = {
        'temp' : temp
    }
    return render(request,'main/temp/survey.html',context)

@active_teacher_required
def survey_tutor(request):
    if request.method == 'POST':
        money = request.POST.get('user_salary', None)
        rec = request.POST.get('user_rec', None)
        email = request.user.email
        temp = SurveyTutor(money=money,rec=rec,email=email)
        temp.save()
        messages.success(request, f'done')
        return redirect('survey-tutor')
    temp = SurveyTutor.objects.latest()
    context = {
        'temp' : temp
    }
    return render(request,'main/temp/survey-tutor.html',context)

def for_student(request):
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
        return redirect('main/temp/for-student.html')
    return render(request,'main/temp/for-student.html')

def for_other(request):
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
        return redirect('main/temp/for-other.html')
    return render(request,'main/temp/for-other.html')

