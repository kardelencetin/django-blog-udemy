import imp
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import CustomUserModel

# Register your models here.

@admin.register(CustomUserModel)

class CustomAdmin(UserAdmin):
    list_display = ('username', 'email')
    fieldsets = UserAdmin.fieldsets + (
        ('Avatar Değiştirme Alanı', {
            'fields': ['avatar']
        }),
    )

# admin.site.register(CustomUserModel, CustomAdmin)
