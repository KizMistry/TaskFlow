from django.contrib.auth.models import User
from .models import Project
from rest_framework import status
from rest_framework.test import APITestCase


class ProjectListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='kiran', password='pass')

    def test_can_list_projects(self):
        kiran = User.objects.get(username='kiran')
        Project.objects.create(owner=kiran, title='Project Test')
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_projects(self):
        self.client.login(username='kiran', password='pass')
        response = self.client.post('/projects/', {'title': 'Project Test'})
        count = Project.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_posts(self):
        response = self.client.post('/projects/', {'title': 'Project Test'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
