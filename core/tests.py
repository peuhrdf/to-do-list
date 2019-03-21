from django.urls import reverse
from django.test import SimpleTestCase


class TodoTestCase(SimpleTestCase):

    def test_new_todo(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='registration/login.html')
