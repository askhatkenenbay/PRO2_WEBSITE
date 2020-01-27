from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from main.models import Course, Theory, TheoryTask, TheoryGraphic, TheoryFormula, TheoryLaw

COURSES = [('chemistry','chemistry'),('physics','physics'),]
class CourseRegisterForm(ModelForm):
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

TASK_TYPES = [('essential','essential'),('understandings','understandings'),]
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
    text = forms.CharField()
    more = forms.TextInput()

    theory_name = forms.HiddenInput()
    course_name = forms.HiddenInput()
    creator_email = forms.HiddenInput()
    class Meta:
        model = TheoryLaw
        fields = ['name','text','more']
