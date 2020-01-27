from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from PIL import Image
from users.managers import CustomUserManager

class Person(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50)
    email = models.EmailField(_('email address'),  primary_key=True)
    password = models.CharField(max_length=1000)
    phone = models.CharField(max_length=25)
    person_type = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','password','phone',person_type]

    objects = CustomUserManager()

    def str(self):
        return self.email
    
      
class Course(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    course_type = models.CharField(max_length=100)
    creator_email = models.CharField(max_length=100)
    # creator_email = models.ForeignKey(Person, on_delete=models.CASCADE)

class Theory(models.Model):
    creator_email = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)

    theory_name = models.CharField(max_length=200, primary_key=True)
    order = models.IntegerField()

class TheoryTask(models.Model):
    creator_email = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    theory_name = models.CharField(max_length=200)

    task_type = models.CharField(max_length=250)
    task = models.CharField(max_length=1000)

class TheoryGraphic(models.Model):
    creator_email = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    theory_name = models.CharField(max_length=200,)

    order = models.IntegerField()
    graphic = models.ImageField(upload_to='graphics')


class TheoryFormula(models.Model):
    creator_email = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    theory_name = models.CharField(max_length=200)

    header = models.CharField(max_length=100)
    main = models.CharField(max_length=100)
    footer = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    # more = models.TextField()

class TheoryLaw(models.Model):
    creator_email = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    theory_name = models.CharField(max_length=200)

    name = models.CharField(max_length=100)
    text = models.CharField(max_length=10000)
    more = models.TextField()




    
      



