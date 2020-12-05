from rest_framework import serializers

from group_manager.models.custom_user import CustomUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'id',
            'email',
            'identity_document'
        )
        read_only_fields = (
            'id',
            'email',
            'identity_document'
        )
