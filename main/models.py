from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from PIL import Image
from users.managers import CustomUserManager
import datetime
class Person(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50)
    email = models.EmailField(_('email address'),  primary_key=True)
    password = models.CharField(max_length=1000)
    phone = models.CharField(max_length=25)
    person_type = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_god = models.BooleanField(default=False)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','password','phone',person_type]

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    
class CourseTaken(models.Model):
    user_email = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    is_paid = models.BooleanField(default=False)
    def __str__(self):
        return self.course_name

class Course(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    course_type = models.CharField(max_length=100)
    creator_email = models.CharField(max_length=100)
    def __str__(self):
        return ""+self.name+"-"+self.course_type

class Theory(models.Model):
    creator_email = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)

    theory_name = models.CharField(max_length=200, primary_key=True)
    order = models.IntegerField()

    def __str__(self):
        return self.course_name+"-"+self.theory_name

class TheoryTask(models.Model):
    creator_email = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    theory_name = models.CharField(max_length=200)

    task_type = models.CharField(max_length=250)
    task = models.CharField(max_length=1000)
    def __str__(self):
        return ""+self.course_name+"-"+self.theory_name+"-"+self.task

class TheoryGraphic(models.Model):
    creator_email = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    theory_name = models.CharField(max_length=200,)

    order = models.IntegerField()
    graphic = models.ImageField(upload_to='graphics')
    def __str__(self):
        return ""+self.course_name+"-"+self.theory_name


class TheoryFormula(models.Model):
    creator_email = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    theory_name = models.CharField(max_length=200)

    header = models.CharField(max_length=100)
    main = models.CharField(max_length=100)
    footer = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    # more = models.TextField()
    def __str__(self):
        return ""+self.course_name+"-"+self.theory_name+"-"+self.header

class TheoryLaw(models.Model):
    creator_email = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    theory_name = models.CharField(max_length=200)

    name = models.CharField(max_length=100)
    text = models.TextField()
    more = models.CharField(max_length=250)
    def __str__(self):
        return ""+self.course_name+"-"+self.theory_name+"-"+self.name


class Homework(models.Model):
    creator_email = models.CharField(max_length=100, default="none")
    course_name = models.CharField(max_length=100)
    is_optional = models.BooleanField()
    order = models.IntegerField()
    homework_name = models.CharField(max_length=100)
    text = models.TextField()
    def __str__(self):
        return ""+self.course_name+"-"+self.homework_name+"-->"+str(self.is_optional)

class HomeworkPoints(models.Model):
    creator_email = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    homework_name = models.CharField(max_length=100)

    points = models.CharField(max_length=250)
    def __str__(self):
        return ""+self.course_name+"-"+self.points

class SurveyStudent(models.Model):
    date = models.DateField(_("Date"), default=datetime.date.today)
    fio = models.CharField(max_length=250, default="empty")
    subject = models.CharField(max_length=500)
    money = models.CharField(max_length=500)
    when =  models.CharField(max_length=500)
    goal = models.CharField(max_length=1000)
    student_name = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    email = models.CharField(max_length=250, default="empty")
    phone = models.CharField(max_length=100)
    class Meta:
        get_latest_by = 'date'
    def __str__(self):
        return ""+self.student_name+"-"+self.goal+"-"+self.email

class SurveyTutor(models.Model):
    email = models.CharField(max_length=250, default="empty")
    subjects = models.CharField(max_length=250, default="empty")
    university = models.CharField(max_length=250, default="empty")
    experience = models.CharField(max_length=250, default="empty")
    price = models.CharField(max_length=250, default="empty")
    time = models.CharField(max_length=250, default="empty")
    class Meta:
        get_latest_by = 'date'
    def __str__(self):
        return ""+self.email+"-"+self.money+"-"+self.rec

class Answer(models.Model):
    answerOne = models.IntegerField()
    answerOneText = models.CharField(max_length=250, default="empty")
    answerTwo = models.IntegerField()
    answerTwoText = models.CharField(max_length=250, default="empty")
    answerThree = models.IntegerField()
    answerThreeText = models.CharField(max_length=250, default="empty")
    answerFourText = models.CharField(max_length=250, default="empty")
    answerFiveText = models.CharField(max_length=250, default="empty")

class Cta(models.Model):
    name = models.CharField(max_length=250, default="empty")
    age = models.IntegerField()

    
      



