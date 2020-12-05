from django.test import TestCase

from group_manager.models.team import Team


class TeamModelTest(TestCase):

    def setUp(self):
        self.test_name = 'test team'

    def test_creation(self):
        old_count = len(Team.objects.all())
        team = Team.objects.create(
            name=self.test_name
        )
        new_count = len(Team.objects.all())

        self.assertIsNotNone(team)
        self.assertTrue(isinstance(team, Team))
        self.assertEqual(team.name, self.test_name)
        self.assertEqual(old_count, new_count - 1)

        team.delete()
