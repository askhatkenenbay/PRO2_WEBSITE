from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from main.models import Person
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserRegisterForm(ModelForm):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    phone = forms.CharField(widget=forms.NumberInput)
    person_type = forms.BooleanField(required=False)
    class Meta:
        model = Person
        fields = ['name','email','phone','person_type','password']

class CustomUserCreationForm(UserCreationForm):
    name = forms.CharField()
    email = forms.EmailField()
    #password = forms.CharField(widget=forms.PasswordInput)
    phone = forms.CharField(widget=forms.NumberInput)
    person_type = forms.BooleanField(required=False)
    class Meta(UserCreationForm):
        model = Person
        fields = ['name','email','phone','person_type']

#no used
class CustomUserChangeForm(UserChangeForm):
    name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField(widget=forms.NumberInput)
    image = forms.ImageField()
    class Meta:
        model = Person
        fields = ('email','name','phone','image')

class PersonUpdateForm(forms.ModelForm):

    #name = forms.CharField()
    #email = forms.EmailField()
    #phone = forms.CharField(widget=forms.NumberInput)
    #image = forms.ImageField()
    class Meta:
        model = Person
        fields = ['name','phone','image']



