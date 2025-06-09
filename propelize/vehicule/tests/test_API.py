from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from ..models import Vehicule
from django.test import TestCase

from rest_framework_simplejwt.tokens import  RefreshToken
from ..serializers import VehiculeSerializer
from user.models import User

class VehiculeAPITest(APITestCase):
    def setUp(self):

        self.user = User.objects.create(
            name='testuser',
            password='testpassword'
        )

        token = RefreshToken.for_user(self.user)
        self.access_token = str(token.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        self.vehicule = Vehicule.objects.create(
            registration_number="123XYZ",
            make="Toyota",
            model="CHR",
            year=2022,
            rentalprice=100.000
        )

        self.vehicule2=Vehicule.objects.create(
            registration_number="123XZZ",
            make="Toyota",
            model="CHR",
            year=2022,
            rentalprice=110.000
        )

        self.vehicules_serilizer = VehiculeSerializer([self.vehicule,self.vehicule2],many=True)


    def test_get_single_vehicule(self):
        url = reverse('vehicule-detail', kwargs={'pk': self.vehicule.pk})

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['model'], "CHR")

    def test_get_all_vehicule(self):
        url = reverse('vehicule-list')

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        self.assertEqual(response.data, self.vehicules_serilizer.data)

class SearchViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            name='testuser',
            password='testpassword'
        )

        token = RefreshToken.for_user(self.user)
        self.access_token = str(token.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        Vehicule.objects.create(registration_number='ABC123', make='Honda' , model='Accord', rentalprice=100.0, year=2020)
        Vehicule.objects.create(registration_number='XYZ789', make='Toyota' , model='Camry', rentalprice=200.0, year=2025)

    def test_search_by_registration_success(self):
        # Arrange
        url = reverse('search_by_registration')
        registration_number = 'ABC123'

        # Act
        response = self.client.get(url, {'registration_number': registration_number})

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['registration_number'], registration_number)

    def test_search_by_registration_missing_param(self):
        # Arrange
        url = reverse('search_by_registration')

        # Act
        response = self.client.get(url)

        # Assert
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())

    def test_search_by_price_success(self):
        # Arrange
        url = reverse('search_by_price')
        max_price = 150

        # Act
        response = self.client.get(url, {'max_price': max_price})

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertLessEqual(float(response.json()[0]['rentalprice']), max_price)


    def test_search_by_price_missing_param(self):
        # Arrange
        url = reverse('search_by_price')

        # Act
        response = self.client.get(url)

        # Assert
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())

    def test_search_by_price_invalid_param(self):
        # Arrange
        url = reverse('search_by_price')
        invalid_price = 'invalid'

        # Act
        response = self.client.get(url, {'max_price': invalid_price})

        # Assert
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())


class VehiculeIntegrationTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            name='testuser',
            password='testpassword'
        )

        token = RefreshToken.for_user(self.user)
        self.access_token = str(token.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_crud_workflow(self):
        #  CREATE
        create_url = reverse('vehicule-create')
        data_create = {
            "registration_number": "ZZ999ZZ",
            "make": "Peugeot",
            "model": "308",
            "year": 2023,
            "rentalprice": 100.0
        }
        response = self.client.post(create_url, data_create, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        vehicule_id = response.data['id']  # récupère l'id créé

        #  READ
        detail_url = reverse('vehicule-detail', kwargs={'pk': vehicule_id})
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['registration_number'], data_create['registration_number'])

        #  UPDATE
        update_url = reverse('vehicule-update', kwargs={'pk': vehicule_id})
        data_update = {
            "registration_number": "ZZ999ZZ",
            "make": "Peugeot",
            "model": "308 GT",
            "year": 2023,
            "rentalprice": 120.0
        }
        response = self.client.patch(update_url, data_update, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['model'], "308 GT")
        self.assertEqual(float(response.data['rentalprice']), 120.0)


        #  DELETE (si tu as un endpoint de suppression)
        delete_url = reverse('vehicule-delete', kwargs={'pk': vehicule_id})
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        #  Vérifier que le véhicule est bien supprimé
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
