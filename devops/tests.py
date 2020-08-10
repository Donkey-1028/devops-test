from django.test import TestCase
from django.urls import reverse


class HomeTest(TestCase):
    url = reverse('devops:home')

    def test_home(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)


# Create your tests here.
