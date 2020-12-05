from django.contrib import admin

from group_manager.models.custom_user import CustomUser
from group_manager.admin.user import CustomUserAdmin
from group_manager.models.team import Team
from group_manager.admin.team import TeamAdmin


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Team, TeamAdmin)
