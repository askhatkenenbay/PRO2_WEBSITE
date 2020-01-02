from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from PIL import Image
from users.managers import CustomUserManager

class Person(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50)
    email = models.EmailField(_('email address'), unique=True, primary_key=True)
    password = models.CharField(max_length=1000)
    phone = models.CharField(max_length=25)
    person_type = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','password','phone']

    objects = CustomUserManager()

    def str(self):
        return self.email
    
      
      
      
  

#
#class Profile(models.Model):
  #  user = models.OneToOneField(Person, on_delete=models.CASCADE)
  #  image = models.ImageField(default='default.jpg', upload_to='profile_pics')
#
   # def __str__(self):
   #     return f'{self.user.email} Profile'

