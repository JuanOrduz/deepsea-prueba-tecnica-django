from django.test import TestCase

from group_manager.models.custom_user import CustomUser


class CustomUserModelTest(TestCase):

    def setUp(self):
        self.test_email = 'testuser1@example.com'
        self.test_password = 'password'

    def test_creation(self):
        old_count = len(CustomUser.objects.all())
        user = CustomUser.objects.create_user(
            email=self.test_email,
            password=self.test_password
        )
        new_count = len(CustomUser.objects.all())

        self.assertIsNotNone(user)
        self.assertTrue(isinstance(user, CustomUser))
        self.assertEqual(user.email, self.test_email)
        self.assertEqual(old_count, new_count - 1)

        user.delete()
