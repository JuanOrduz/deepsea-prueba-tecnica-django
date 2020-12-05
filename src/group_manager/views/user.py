from rest_framework import generics

from group_manager.serializers.user import UserSerializer
from group_manager.models.custom_user import CustomUser


class UserListView(generics.ListAPIView):
    name = 'USER_LIST_VIEW'
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
