from django.contrib.auth.models import User
from .models import Task
from rest_framework import status
from rest_framework.test import APITestCase

class ProfileListViewTests(APITestCase):
  def setUp(self):
    User.objects.create_user(username='billy', password='pass')

  def test_can_list_tasks(self):
    kiran = User.objects.get(username='kiran')
    Task.objects.create(owner=billy, title='Task Test')
    response = self.client.get('/tasks/')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    print(response.data)
    print(len(response.data))
