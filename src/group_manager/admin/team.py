from django.contrib import admin

from group_manager.models.team import Team


class UserInline(admin.TabularInline):
    model = Team.users.through
    extra = 2


class TeamAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ['name', 'image']}),
    )
    inlines = [UserInline]
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'image'),
        }),
    )
    list_display = ('name', 'created_at')
    ordering = ('name',)
