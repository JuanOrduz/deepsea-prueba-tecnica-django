from django.urls import path, re_path

from group_manager.views import user
from group_manager.views import team

urlpatterns = [
    path('users/',
         user.UserListView.as_view(),
         name=user.UserListView.name
         ),
    path('teams/',
         team.TeamListCreateView.as_view(),
         name=team.TeamListCreateView.name
         ),
    re_path('^teams/(?P<team_id>[0-9a-f-]+)$',
            team.TeamRetrieveUpdateDeleteView.as_view(),
            name=team.TeamRetrieveUpdateDeleteView.name
            ),
]
