from django.test import TestCase

from group_manager.models.custom_user import CustomUser
from group_manager.serializers.user import UserSerializer


class UserSerializerTest(TestCase):
    def setUp(self):
        self.test_user = CustomUser.objects.create_user(
            email='testuser1@example.com',
            password='password'
        )

    def tearDown(self):
        self.test_user.delete()

    def test_deserialization(self):
        serializer = UserSerializer(instance=self.test_user)

        self.assertEqual(set(serializer.data.keys()), {'id', 'email', 'identity_document'})
        self.assertEqual(self.test_user.id, serializer.data['id'])
        self.assertEqual(self.test_user.email, serializer.data['email'])
        self.assertEqual(self.test_user.identity_document, serializer.data['identity_document'])
