from rest_framework import serializers

from group_manager.models.team import UserTeam


class UserTeamSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    identity_document = serializers.SerializerMethodField()

    class Meta:
        model = UserTeam
        fields = (
            'id',
            'email',
            'identity_document',
            'joined_at',
        )
        read_only_fields = (
            'id',
            'email',
            'identity_document',
            'joined_at',
        )

    def get_id(self, obj):
        return obj.user.id

    def get_email(self, obj):
        return obj.user.email

    def get_identity_document(self, obj):
        return obj.user.identity_document
