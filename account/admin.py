from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'user_name', 'last_name')
    last_filter = ('email', 'user_name', 'is_active', 'is_superuser')
    ordering = ('-date_joined',)
    list_display = ('email', 'user_name', 'is_active', 'is_superuser')
    readonly_fields = ['date_joined', 'last_login']


fieldsets = (
    (None, {'fields': ('email', 'user_name', )}),
    ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    ('Personal', {'fields': ('about', 'last_name', 'first_name')}),
)


add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('email', 'user_name', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')
    }),
)

admin.site.register(Account, UserAdminConfig)
