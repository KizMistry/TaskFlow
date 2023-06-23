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


class ProjectDetailViewTests(APITestCase):
    def setUp(self):
        kiran = User.objects.create_user(username='kiran', password='pass')
        jordan = User.objects.create_user(username='jordan', password='pass')
        Project.objects.create(
            owner=kiran, title='Project Test', description='Kirans project details'
        )
        Project.objects.create(
            owner=jordan, title='Project Test', description='Jordans project details'
        )

    def test_can_retrieve_project_using_valid_id(self):
        response = self.client.get('/projects/1/')
        self.assertEqual(response.data['title'], 'Project Test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_project_using_invalid_id(self):
        response = self.client.get('/posts/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_project(self):
        self.client.login(username='kiran', password='pass')
        response = self.client.put('/projects/1/', {'title': 'TaskFlow'})
        project = Project.objects.filter(pk=1).first()
        self.assertEqual(project.title, 'TaskFlow')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_project(self):
        self.client.login(username='kiran', password='pass')
        response = self.client.put('/projects/2/', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)