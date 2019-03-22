from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .models import Todo


class TodoTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='teste', password='teste')
        self.user.save()

    def test_login(self):
        #tentando logar
        login = self.client.login(username='teste', password='teste')
        self.assertEquals(login, True)

        #tentando acessando url após logar
        response = self.client.get(reverse('new_to_do'))
        self.assertEqual(response.status_code, 200)

        # verificando usuario logado
        self.assertEqual(str(response.context['user']), 'teste')

        # criando novo To_do
        self.client.post('/todo/new/', {'title': "teste_title", 'text': "teste_text"})

        # verificando instancia do To_do
        self.assertIsInstance(Todo.objects.last(), Todo)

        # verificando dados do To_do inserido anteriormente
        self.assertEqual(Todo.objects.last().title, 'teste_title')
        self.assertEqual(Todo.objects.last().text, 'teste_text')
