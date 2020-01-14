from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main-home'),
    path('personal-page/',views.personal_page, name='main-personal_page'),
    path('theory/',views.theory, name='theory'),
    path('theory-practice/', views.practice, name='practice'),
    path('homework/',views.homework, name='homework'),
    path('test/',views.test, name='test'),
    path('formula/',views.formula, name='formula'),
    path('homework/solve/', views.homeworkNext, name='homeworkNext'),
]