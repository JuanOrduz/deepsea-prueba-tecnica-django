from django.test import TestCase
from django.urls import reverse

from group_manager.models.custom_user import CustomUser


class UserListViewTest(TestCase):
    def setUp(self):
        self.list_url = reverse('USER_LIST_VIEW')
        self.test_user = CustomUser.objects.create_user(
            email='testuser1@example.com',
            password='password'
        )

    def tearDown(self):
        self.test_user.delete()

    def test_list(self):
        response = self.client.get(self.list_url)
        users_json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(users_json) > 0)
