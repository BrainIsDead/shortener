from django.test import TestCase
from .models import User


class UserTest(TestCase):
    def setUp(self):
        User.objects.create(
            email='test_user@test.com',
            password=User.objects.make_random_password()
        )

    def test_user_str(self):
        user = User.objects.get(email='test_user@test.com')
        self.assertEqual(user.__str__(), 'test_user@test.com')
