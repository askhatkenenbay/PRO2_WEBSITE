from django.contrib import admin
from .models import Person, CourseTaken, SurveyStudent,SurveyTutor
from django.contrib.auth.admin import UserAdmin
from users.forms import CustomUserCreationForm, CustomUserChangeForm
from .forms import CourseTakenForm, CourseTakenChangeForm

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
    list_display = ('email', 'student_name','client_name','goal','subject','money','date')

class SurveyTutorAdmin(admin.ModelAdmin):
    model = SurveyTutor
    list_display = ('email', 'date','money','rec')

admin.site.register(Person, CustomUserAdmin)
admin.site.register(CourseTaken,CourseTakenAdmin)
admin.site.register(SurveyStudent, SurveyStudentAdmin)
admin.site.register(SurveyTutor,SurveyTutorAdmin)

