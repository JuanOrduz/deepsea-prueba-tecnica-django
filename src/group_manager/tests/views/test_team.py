import json

from django.test import TestCase
from django.urls import reverse

from group_manager.models.custom_user import CustomUser
from group_manager.models.team import Team


class TeamListCreateViewTest(TestCase):
    def setUp(self):
        self.list_create_url = reverse('TEAM_LIST_CREATE_VIEW')
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

    def test_list(self):
        response = self.client.get(self.list_create_url)
        teams_json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(teams_json) > 0)

    def test_create(self):
        data = {
            'name': 'test team 2',
            'users_ids': [self.test_user.id]
        }
        response = self.client.post(
            self.list_create_url,
            json.dumps(data),
            content_type="application/json")
        response_json = response.json()

        team = Team.objects.get(id=response_json['id'])

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_json['id'], team.id)
        self.assertEqual(response_json['name'], team.name)

        team.delete()


class TeamRetrieveUpdateDeleteViewTest(TestCase):
    def setUp(self):
        self.test_user = CustomUser.objects.create_user(
            email='testuser1@example.com',
            password='password'
        )
        self.test_team = Team.objects.create(
            name='test team 1'
        )
        self.retrieve_update_ur = reverse('TEAM_RETRIEVE_UPDATE_DESTROY_VIEW',
                                                kwargs={'team_id': self.test_team.id})

    def tearDown(self):
        self.test_user.delete()
        self.test_team.delete()

    def test_retrieve(self):
        response = self.client.get(self.retrieve_update_ur)
        team_json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(set(team_json.keys()), {'id', 'name', 'image', 'created_at', 'updated_at', 'users'})

    def test_update(self):
        updated_name = self.test_team.name + ' Updated'
        data = {
            'name': updated_name,
            'users_ids': [self.test_user.id]
        }

        response = self.client.put(self.retrieve_update_ur,
                                   json.dumps(data),
                                   content_type="application/json")
        team_json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(set(team_json.keys()), {'id', 'name', 'image', 'created_at', 'updated_at', 'users'})
        self.assertEqual(data['name'], updated_name)

    def test_delete(self):
        test_team_delete = Team.objects.create(
            name='test team 2'
        )

        self.delete_url = reverse('TEAM_RETRIEVE_UPDATE_DESTROY_VIEW',
                                                kwargs={'team_id': test_team_delete.id})

        response = self.client.delete(self.delete_url)

        self.assertEqual(response.status_code, 204)
