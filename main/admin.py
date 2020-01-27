from django.contrib import admin
from .models import Person
from django.contrib.auth.admin import UserAdmin
from users.forms import CustomUserCreationForm, CustomUserChangeForm


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
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(Person, CustomUserAdmin)


