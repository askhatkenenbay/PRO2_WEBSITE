from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main-home'),
    path('personal-page/',views.personal_page, name='main-personal_page'),
]