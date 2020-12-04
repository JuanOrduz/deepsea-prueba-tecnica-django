from rest_framework import serializers

from group_manager.models.custom_user import CustomUser
from group_manager.models.team import Team
from group_manager.serializers.user_team import UserTeamSerializer
from group_manager.business_logic import team as team_logic


class TeamSerializer(serializers.ModelSerializer):
    users = UserTeamSerializer(
        source='userteam_set',
        many=True,
        read_only=True
    )

    # name = serializers.CharField(
    #     required=True,
    #     write_only=True
    # )
    #
    # image = serializers.CharField(
    #     required=True,
    #     write_only=True
    # )

    users_ids = serializers.ListField(
        required=True,
        write_only=True,
        child=serializers.CharField()
    )

    class Meta:
        model = Team
        fields = (
            'id',
            'name',
            'image',
            'created_at',
            'updated_at',
            'users',
            'users_ids',
        )
        read_only_fields = (
            'id',
            'created_at',
            'updated_at',
            'users',
        )

    def create(self, validated_data):
        users_ids = validated_data.pop('users_ids')
        team = Team.objects.create(**validated_data)
        team = team_logic.assign_users(team, users_ids)
        return team

    def update(self, instance, validated_data):
        instance = super(TeamSerializer, self).update(instance, validated_data)
        instance = team_logic.update_users(instance, validated_data['users_ids'])
        return instance
