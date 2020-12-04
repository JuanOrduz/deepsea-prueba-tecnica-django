from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from group_manager.models.custom_user import CustomUser


class GroupInline(admin.TabularInline):
    model = CustomUser.teams.through
    extra = 2


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ['identity_document', 'email']}),
        ('Permissions', {'fields': ('is_active', 'is_superuser')}),
    )
    inlines = [GroupInline]
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_superuser'),
        }),
    )
    list_display = ('email', 'identity_document', 'is_superuser')
    list_filter = ()
    ordering = ('email',)
