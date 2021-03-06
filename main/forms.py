from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from main.models import Course, Theory, TheoryTask, TheoryGraphic, TheoryFormula, TheoryLaw, CourseTaken, Homework, HomeworkPoints, SurveyStudent, Answer


class CourseTakenForm(ModelForm):
    user_email = forms.CharField(required=True)
    course_name = forms.CharField(required=True)
    is_paid = forms.BooleanField(required=True)
    class Meta:
        model = CourseTaken
        fields = ['user_email','course_name','is_paid']

class CourseTakenChangeForm(UserChangeForm):
    user_email = forms.CharField()
    course_name = forms.CharField()
    is_paid = forms.BooleanField(required=True)
    class Meta:
        model = CourseTaken
        fields = ('user_email','course_name','is_paid')


COURSES = [('chemistry','chemistry'),('physics','physics'),]
class CourseRegisterForm(ModelForm):
    name =  forms.CharField(required=True)
    course_type = forms.MultipleChoiceField(required=True,widget=forms.CheckboxSelectMultiple,choices=COURSES,)
    creator_email = forms.CharField(required=True)
    class Meta:
        model = Course
        fields = ['name','course_type','creator_email']

class CourseChangeForm(UserChangeForm):
    name =  forms.CharField(required=True)
    course_type = forms.MultipleChoiceField(required=True,widget=forms.CheckboxSelectMultiple,choices=COURSES,)
    creator_email = forms.CharField(required=True)
    class Meta:
        model = Course
        fields = ['name','course_type','creator_email']

class TheoryRegisterForm(ModelForm):
    theory_name = forms.CharField(required=True)
    order = forms.IntegerField()
    course_name = forms.HiddenInput()
    creator_email = forms.HiddenInput()
    class Meta:
        model = Theory
        fields = ['theory_name','order']

TASK_TYPES = [('essential','essential'),('understandings','understandings'),('app','app'),]
class TheoryTaskRegisterForm(ModelForm):
    task_type =  forms.MultipleChoiceField(required=True,widget=forms.CheckboxSelectMultiple,choices=TASK_TYPES,)
    task = forms.CharField(required=True)

    theory_name = forms.HiddenInput()
    course_name = forms.HiddenInput()
    creator_email = forms.HiddenInput()
    class Meta:
        model = TheoryTask
        fields = ['task_type','task']

class TheoryGraphicRegisterForm(ModelForm):
    image = forms.ImageField(required=True)
    order = forms.IntegerField(required=True)

    theory_name = forms.HiddenInput()
    course_name = forms.HiddenInput()
    creator_email = forms.HiddenInput()
    class Meta:
        model = TheoryGraphic
        fields = ['image','order']

CATEGORY = [('category 1','category 1'),('category 2','category 2'),('category 3','category 3'),]
class TheoryFormulaRegisterForm(ModelForm):
    header = forms.CharField()
    main = forms.CharField(required=True)
    footer = forms.CharField()
    category = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=CATEGORY,)
    # more = forms.TextInput()

    theory_name = forms.HiddenInput()
    course_name = forms.HiddenInput()
    creator_email = forms.HiddenInput()
    class Meta:
        model = TheoryFormula
        fields = ['header','main','footer','category']

class TheoryLawRegisterForm(ModelForm):
    name = forms.CharField()
    text = forms.TextInput()
    more = forms.CharField()

    theory_name = forms.HiddenInput()
    course_name = forms.HiddenInput()
    creator_email = forms.HiddenInput()
    class Meta:
        model = TheoryLaw
        fields = ['name','more','text']

class HomeworkForm(ModelForm):
    course_name = forms.HiddenInput()
    creator_email = forms.HiddenInput()

    text = forms.TextInput()
    name = forms.CharField()
    order = forms.IntegerField(required=True)
    class Meta:
        model = Homework
        fields = ['name','order','text']

class HomeworkPointsForm(ModelForm):
    course_name = forms.HiddenInput()
    creator_email = forms.HiddenInput()
    homework_name = forms.HiddenInput()

    point = forms.CharField()
    class Meta:
        model = HomeworkPoints
        fields = ['point']

class SurveyStudentForm(ModelForm):
    date = forms.DateField()
    fio = forms.CharField()
    subject = forms.CharField()
    money = forms.CharField()
    when = forms.CharField()
    goal = forms.CharField()
    student_name = forms.CharField()
    language = forms.CharField()
    email = forms.HiddenInput()
    phone = forms.CharField()
    class Meta:
        model = SurveyStudent
        fields = ['date','fio','subject','money','when','goal','student_name','language','phone']

class AnswerForm(ModelForm):
    one = forms.IntegerField()
    oneText = forms.CharField()
    two = forms.IntegerField()
    twoText = forms.CharField()
    three = forms.IntegerField()
    threeText = forms.CharField()
    fourText = forms.CharField()
    fiveText = forms.CharField()
    email = forms.HiddenInput()
    class Meta:
        model = Answer
        fields = ['one','oneText','two','twoText','three','threeText','fourText','fiveText']
   



