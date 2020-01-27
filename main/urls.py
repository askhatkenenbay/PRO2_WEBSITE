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
    path('ru/',views.home_ru, name='main-home-ru'),
    path('personal-page/create-course/',views.create_course,name="create-course"),
    path('personal-page/create-course/create-theory/',views.create_theory,name="create-theory"),
    path('personal-page/create-course/create-theory-task/',views.create_theory_task,name="create-theory-task"),
    path('personal-page/create-course/create-theory-graphic/',views.create_theory_graphic,name="create-theory-graphic"),
    path('personal-page/create-course/create-theory-formula/',views.create_theory_formula,name="create-theory-formula"),
    path('personal-page/create-course/create-theory-law/',views.create_theory_law,name="create-theory-law"),
    path('personal-page/my-courses/',views.my_courses,name="my-courses")
]