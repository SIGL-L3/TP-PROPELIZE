from django.urls import  reverse
from rest_framework.test import  APITestCase
from rest_framework import  status
from ..models import User

class UsuerAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            name="Emile",
            password="emile@43215",
        )

    def test_user_creation(self):
        url = reverse('create-user')

        data = {
            "name" : "John",
            "password" : "john@43215"
        }

        response = self.client.post(url,data,format='json')

        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'],"John")

    def test_creation_user_with_same_name(self):
        url = reverse('create-user')

        data={
            "name" : "Emile",
            "password" : "emile@43215",
        }
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

    def test_user_creation_with_blank_fields(self):
        url = reverse('create-user')

        data = {
            "name": "",
            "password": ""
        }

        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

    def test_update_user(self):
        url = reverse('update-user',kwargs={'pk':self.user.pk})
        data = {
            "name":"Emile2"
        }

        response = self.client.patch(url,data=data,format='json')

        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['name'],"Emile2")

    def test_update_user_wit_unexistant_pk(self):
        url = reverse('update-user',kwargs={'pk':100000})
        data = {
            "name":"Emile2"
        }
        response = self.client.patch(url,data=data,format='json')

        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)

    def test_user_login(self):
        url = reverse('token_obtain')

        data = {"name":"Emile","password":"emile@43215"}

        response = self.client.post(url,data=data,format='json')

        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertIn('access',response.data)
        self.assertIn('refresh',response.data)

    def test_user_login_with_invalid_data(self):

        url = reverse('token_obtain')
        data = {"name": "noregisteruser", "password": ""}

        response = self.client.post(url, data=data, format='json')

        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)