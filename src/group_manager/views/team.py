from rest_framework import generics

from group_manager.serializers.team import TeamSerializer
from group_manager.models.team import Team


class TeamListCreateView(generics.ListCreateAPIView):
    name = 'TEAM_LIST_CREATE_VIEW'
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    name = 'TEAM_RETRIEVE_UPDATE_DESTROY_VIEW'
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'team_id'
