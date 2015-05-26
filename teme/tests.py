from django.test import TestCase
from django.test import Client
from django.test.utils import setup_test_environment


class TemeTests(TestCase):
    def test_home(self):
        setup_test_environment()
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_search_box(self):
        setup_test_environment()
        client = Client()
        response = client.get('/')
        self.assertTrue('Cauta' in str(response.content))

    def test_courses(self):
        setup_test_environment()
        client = Client()
        response = client.get('/courses')
        self.assertEqual(response.status_code, 200)

    def test_teachers(self):
        setup_test_environment()
        client = Client()
        response = client.get('/teachers')
        self.assertEqual(response.status_code, 200)
