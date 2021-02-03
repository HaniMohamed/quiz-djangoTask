from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase


class AccountTests(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create_user(
            username='admin',
            password='admin123',
            is_staff=True,
            is_superuser=False)

        self.super_user = User.objects.create_user(
            username='superuser',
            password='superuser123',
            is_staff=False,
            is_superuser=True)

    def test_not_user(self):
        response = self.client.get('http://localhost:8000/api/v1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_user(self):
        client = APIClient()
        client.force_authenticate(user=self.admin_user)
        response = client.get('http://localhost:8000/api/v1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_super_user(self):
        client = APIClient()
        client.force_authenticate(user=self.super_user)
        response = client.get('http://localhost:8000/api/v1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
