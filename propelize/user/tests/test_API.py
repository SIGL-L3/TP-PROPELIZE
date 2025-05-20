from django.urls import  reverse
from rest_framework.test import  APITestCase
from rest_framework import  status
from ..models import User

class UserAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            name="Emile",
            password="emile@43215",
        )
        self.login_url = reverse('token_obtain')
        self.username = "Emile"
        self.password = "emile@43215"


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

    def test_update_user_wit_nonexistant_pk(self):
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
        
        
    def test_user_login_failure_wrong_password(self):
        response = self.client.post(self.login_url, {
            'name': self.username,
            'password': 'wrongpassword'
        }, format='json')
        self.assertEqual(response.status_code, 401)

    def test_user_login_wrong_password(self):
        response = self.client.post(self.login_url, {
            'name': self.username,
            'password': 'wrongpassword'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_login_nonexistent_user(self):
        response = self.client.post(self.login_url, {
            'name': 'unknownuser',
            'password': 'any-password'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_login_missing_username(self):
        response = self.client.post(self.login_url, {
            'password': self.password
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_login_missing_password(self):
        response = self.client.post(self.login_url, {
            'name': self.username
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_login_inactive_user(self):
        self.user.is_active = False
        self.user.save()
        response = self.client.post(self.login_url, {
            'name': self.username,
            'password': self.password
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        
        
        
    def test_user_integration_workflow(self):
        # Création de l’utilisateur
        create_url = reverse('create-user')
        user_data = {
            'name': 'integration_user',
            'password': 'TestPassword123'
        }
        response = self.client.post(create_url, user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'integration_user')

        #  Connexion de l’utilisateur pour obtenir les tokens
        login_url = reverse('token_obtain')
        login_data = {
            'name': 'integration_user',
            'password': 'TestPassword123'
        }
        response = self.client.post(login_url, login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        token = response.data['access']
        headers = {'HTTP_AUTHORIZATION': f'Bearer {token}'}

        #  Mise à jour du nom d’utilisateur
        user_id = response.data.get('user', {}).get('id') or User.objects.get(name='integration_user').id
        update_url = reverse('update-user', kwargs={'pk': user_id})
        update_data = {'name': 'integration_user_updated'}
        response = self.client.patch(update_url, data=update_data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'integration_user_updated')

        #  Suppression de l’utilisateur
        delete_url = reverse('delete-user', kwargs={'pk': user_id})
        response = self.client.delete(delete_url, **headers)
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_204_NO_CONTENT])

        # Vérification que l’utilisateur est bien supprimé
        self.assertFalse(User.objects.filter(pk=user_id).exists())
