from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from users.forms import CustomUserCreationForm, CustomUserChangeForm
from .forms import *

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Person
    list_display = ('email', 'name', 'phone','person_type','is_paid','is_god',)
    list_filter = ('email', 'name', 'phone','person_type','is_paid','is_god',)
    list_editable = ('person_type','is_paid','is_god',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('person_type','is_paid','is_god',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','name','phone','person_type','is_paid', 'password1', 'password2','is_god')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

class CourseTakenAdmin(admin.ModelAdmin):
    add_form = CourseTakenForm
    form = CourseTakenChangeForm
    model = CourseTaken
    list_display = ('user_email', 'course_name','is_paid')
    list_filter = ('user_email', 'course_name','is_paid')
    list_editable = ('is_paid',)
    fieldsets = (
        (None, {'fields': ('user_email', 'course_name','is_paid')}),
        ('Permissions', {'fields': ()}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_email', 'course_name','is_paid')}
        ),
    )
    search_fields = ('user_email',)
    ordering = ('user_email',)


class SurveyStudentAdmin(admin.ModelAdmin):
    model = SurveyStudent
    list_display = ('goal','subject','money','date','email')

class SurveyTutorAdmin(admin.ModelAdmin):
    model = SurveyTutor
    list_display = ('email', 'time','price','subjects')

class AnswerAdmin(admin.ModelAdmin):
    model = Answer
    list_display = ('answerOne', 'answerOneText','answerTwo','answerTwoText','answerThree','answerThreeText','answerFourText','answerFiveText')

class CourseAdmin(admin.ModelAdmin):
    add_form = CourseRegisterForm
    model = Course
    list_display = ('name', 'course_type', 'creator_email',)
    list_filter = ('name', 'course_type', 'creator_email',)
    ordering = ('creator_email',)

class TheoryAdmin(admin.ModelAdmin):
    add_form = TheoryRegisterForm
    model = Theory
    list_display = ('creator_email',"course_name","theory_name","order",)
    list_filter = ('creator_email',"course_name","theory_name","order",)
    ordering = ('creator_email',)

class TheoryTaskAdmin(admin.ModelAdmin):
    add_form = TheoryTaskRegisterForm
    model = TheoryTask
    list_display = ('creator_email',"course_name","theory_name","task_type","task",)
    list_filter = ('creator_email',"course_name","theory_name","task_type","task",)
    ordering = ('creator_email',)

class TheoryGraphicAdmin(admin.ModelAdmin):
    add_form = TheoryGraphicRegisterForm
    model = TheoryGraphic
    list_display = ('creator_email',"course_name","theory_name","order","graphic")
    list_filter = ('creator_email',"course_name","theory_name","order","graphic")
    ordering = ('creator_email',)

class TheoryFormulaAdmin(admin.ModelAdmin):
    add_form = TheoryFormulaRegisterForm
    model = TheoryFormula
    list_display = ('creator_email',"course_name","theory_name","header","main","footer","category",)
    list_filter = ('creator_email',"course_name","theory_name","header","main","footer","category",)
    ordering = ('creator_email',)

class TheoryLawAdmin(admin.ModelAdmin):
    add_form = TheoryRegisterForm
    model = Theory
    list_display = ('creator_email',"course_name","theory_name","name","text","more",)
    list_filter = ('creator_email',"course_name","theory_name","name","text","more",)
    ordering = ('creator_email',)



admin.site.register(Person, CustomUserAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(CourseTaken,CourseTakenAdmin)
admin.site.register(SurveyStudent, SurveyStudentAdmin)
admin.site.register(SurveyTutor,SurveyTutorAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Theory,TheoryAdmin)

admin.site.register(TheoryTask,TheoryTaskAdmin)
admin.site.register(TheoryGraphic,TheoryGraphicAdmin)
admin.site.register(TheoryFormula,TheoryFormulaAdmin)
admin.site.register(TheoryLaw,TheoryLawAdmin)