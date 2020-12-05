from django.test import TestCase

from group_manager.models.custom_user import CustomUser
from group_manager.models.team import Team
from group_manager.serializers.team import TeamSerializer


class TeamSerializerTest(TestCase):
    def setUp(self):
        self.test_user = CustomUser.objects.create_user(
            email='testuser1@example.com',
            password='password'
        )
        self.test_team = Team.objects.create(
            name='test team 1'
        )

    def tearDown(self):
        self.test_user.delete()
        self.test_team.delete()

    def test_serialization(self):
        data = {
            'name': 'test team 2',
            'users_ids': [self.test_user.id]
        }

        serializer = TeamSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        team = serializer.create(data)

        self.assertTrue(isinstance(team, Team))
        self.assertEqual(team.name, data['name'])

    def test_deserialization(self):
        serializer = TeamSerializer(instance=self.test_team)

        self.assertEqual(set(serializer.data.keys()), {'id', 'name', 'image', 'created_at', 'updated_at', 'users'})
        self.assertEqual(self.test_team.id, serializer.data['id'])
        self.assertEqual(self.test_team.name, serializer.data['name'])
