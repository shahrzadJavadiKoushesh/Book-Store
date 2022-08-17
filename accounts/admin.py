from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'age', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (    # age added to CustomerUserChangeForm
        (None, {'fields': ('age', )}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (    # age added to CustomUserCreationForm
        (None, {'fields': ('age',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
