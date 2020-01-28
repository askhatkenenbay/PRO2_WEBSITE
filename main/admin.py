from django.contrib import admin
from .models import Person, CourseTaken
from django.contrib.auth.admin import UserAdmin
from users.forms import CustomUserCreationForm, CustomUserChangeForm
from .forms import CourseTakenForm, CourseTakenChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Person
    list_display = ('email', 'name', 'phone','person_type','is_paid',)
    list_filter = ('email', 'name', 'phone','person_type','is_paid',)
    list_editable = ('person_type','is_paid',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('person_type','is_paid',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','name','phone','person_type','is_paid', 'password1', 'password2')}
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


admin.site.register(Person, CustomUserAdmin)
admin.site.register(CourseTaken,CourseTakenAdmin)

