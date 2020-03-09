from django.test import TestCase
from .models import Link


class LinkTest(TestCase):
    def setUp(self):
        Link.objects.create(full_url='https://www.google.com/')

    def test_link_str(self):
        link = Link.objects.get(full_url='https://www.google.com/')
        self.assertEqual(link.__str__(), 'https://www.google.com/')
